// A_StandingOvation.cpp : main project file.

#include "stdafx.h"

using namespace System;

System::Int32 RunTest (System::String^ test)
{
    array<System::String^>^ split = test->Split();
    System::Int32 added = 0;
    System::Int32 total = 0;
    System::Int32 Levels = System::Convert::ToInt32(split[0]);
    for (System::Int32 i=0; i<Levels+1; i++)
    {
        System::Int32 AtLevel = System::Convert::ToInt32(split[1]->Substring(i,1));
        // not sure if this outer check is necessary
        if (AtLevel)
        {
            if (total < i)
            {
                added += (i-total);
                total = i;
            }
        }
        total += AtLevel;
    }
    return added;
}
int main(array<System::String ^> ^args)
{
    System::IO::TextReader^ rdr = gcnew System::IO::StreamReader(args[0]);
    System::IO::TextWriter^ wtr = gcnew System::IO::StreamWriter(args[0]+".txt");
    System::Int32 NumTests = System::Convert::ToInt32 (rdr->ReadLine());
    for (System::Int32 i=0; i<NumTests; i++)
    {
        wtr->WriteLine ("Case #"+(i+1).ToString()+": "+RunTest(rdr->ReadLine()).ToString());
    }
    rdr->Close();
    wtr->Close();
    return 0;
}
