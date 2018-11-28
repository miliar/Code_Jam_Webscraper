// B.cpp : main project file.

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
        System::String^ testdata;
        System::Int32 N = System::Convert::ToInt32 (rdr->ReadLine());
        wtr->Write ("Case #"+(i+1).ToString()+":");
        System::Console::Write ("Case #"+(i+1).ToString()+":");

        testdata = "";
        for (System::Int32 i=0; i<2*N-1; i++)
        {
            testdata += rdr->ReadLine() + System::Environment::NewLine;
        }
        System::String^ result = RunTest(testdata);
        wtr->WriteLine (result);
        System::Console::WriteLine (result);
    }
    rdr->Close();
    wtr->Close();
    return 0;
}

System::String^ RunTest (System::String^ str)
{
    System::String^ retval = "";
    // process inputs here
    array<System::String^>^ delimit = gcnew array<System::String^>(1);
    delimit[0] = System::Environment::NewLine;
    array<System::String^>^ lines = str->Split(delimit, System::StringSplitOptions::RemoveEmptyEntries);
    
    array<System::Int32>^ freq = gcnew array<System::Int32>(2500);
    for (System::Int32 i=0; i<lines->Length; i++)
    {
        array<System::String^>^ strs = lines[i]->Split(' ');
        for (System::Int32 j=0; j<strs->Length; j++)
        {
            freq[System::Convert::ToInt32(strs[j])-1]++;
        }
    }
    //array<System::Int32>^ Ns = gcnew array<System::Int32>((lines->Length+1)/2);
    for (System::Int32 i=0; i<freq->Length; i++)
    {
        if (freq[i] & 1)
        {
            retval += " " + (i+1);
        }
    }

    //for (System::Int32 i=0; i<Ns->GetLength(0); i++)
    //{
    //    System::Int32 min = 2501;
    //    System::Int32 idx = 0;
    //    for (System::Int32 j=0; j<Ns->GetLength(0); j++)
    //    {
    //        if (Ns[i] < min)
    //        {
    //            min = Ns[i];
    //            idx = i;
    //        }
    //    }
    //    retval += " " + min;
    //    Ns[min] = 2501;
    //}
    return retval;
}