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

System::String^ Optimize (System::String^ str)
{
    System::Char BestChar;
    BestChar = str[0];
    for (System::Int32 i=1; i<str->Length; i++)
    {
        if (str[i] > BestChar)
        {
            BestChar = str[i];
        }
    }
    // for all that match best char
    System::String^ bestString = "0000";
    for (System::Int32 i=str->Length-1; i>=0; i--)
    {
        if (str[i] == BestChar)
        {
            System::String^ thisStr;
            if (i != 0)
            {
                thisStr = Optimize (str->Substring(0,i));
                thisStr = str[i] + thisStr;
                thisStr += str->Substring(i+1,str->Length-i-1);
            }
            else
            {
                thisStr = str;
            }
            if (System::String::Compare (thisStr, bestString) > 0)
            {
                bestString = thisStr;
                break;
            }
        }
    }
    return bestString;
}

System::String^ RunTest (System::String^ str)
{
    System::String^ retval = "";
    // process inputs here
    //array<System::String^>^ delimit = gcnew array<System::String^>(1);
    //delimit[0] = System::Environment::NewLine;
    //array<System::String^>^ lines = str->Split(delimit, System::StringSplitOptions::None);
    //for (System::Int32 i=0; i<lines->Length; i++)
    //{
    //    array<System::String^>^ strs = lines[i]->Split(' ');
    //    switch (i)
    //    {
    //    case 0:
    //        break;
    //    default:
    //        break;
    //    }
    //}
    // run test here
    retval = Optimize(str);
    return retval;
}