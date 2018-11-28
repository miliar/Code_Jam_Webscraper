// A.cpp : main project file.

#include "stdafx.h"

using namespace System;

System::String^ RunTest (System::String^ str);

int main(array<System::String ^> ^args)
{
    System::IO::TextReader^ rdr = gcnew System::IO::StreamReader(args[0]);
    System::String^ outname = args[0]->Substring(0,args[0]->LastIndexOf("."))+".out";
    System::IO::TextWriter^ wtr = gcnew System::IO::StreamWriter(outname);
    System::Int32 NumTests = System::Convert::ToInt32 (rdr->ReadLine());
    for (System::Int32 i=0; i<NumTests; i++)
    {
        wtr->Write ("Case #"+(i+1).ToString()+": ");
        System::Console::Write ("Case #"+(i+1).ToString()+": ");
        System::String^ result = RunTest(rdr->ReadLine());
        wtr->WriteLine (result);
        System::Console::WriteLine (result);
    }
    rdr->Close();
    wtr->Close();
    return 0;
}

System::String^ RunTest (System::String^ str)
{
    array<System::String^>^ Numbers = gcnew array<System::String^> {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    array<System::Char>^ TestChars = gcnew array<System::Char> {'Z','O','W','H','U','F','X','V','G','E'};
    array<System::Int32>^ Order = gcnew array<System::Int32> {0,2,4,6,8,1,3,5,7,9};
    array<System::Int32>^ freq = gcnew array<System::Int32>(10);

    System::String^ retval = "";
    for (System::Int32 i=0; i<Order->Length; i++)
    {
        System::Int32 idx = str->IndexOf(TestChars[Order[i]]);
        while (idx != -1)
        {
            freq[Order[i]]++;
            for (System::Int32 j=0; j<Numbers[Order[i]]->Length; j++)
            {
                System::Int32 idx2 = str->IndexOf(Numbers[Order[i]][j]);
                str = str->Substring(0,idx2) + str->Substring(idx2+1,str->Length-idx2-1);
            }
            idx = str->IndexOf(TestChars[Order[i]]);
        }
    }
    for (System::Int32 i=0; i<freq->Length; i++)
    {
        for (System::Int32 j=0; j<freq[i]; j++)
            retval += i.ToString();
    }
    return retval;
}
