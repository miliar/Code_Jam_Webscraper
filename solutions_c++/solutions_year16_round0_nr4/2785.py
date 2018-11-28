// D_Fractiles.cpp : main project file.

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
        System::String^ result = RunTest(rdr->ReadLine());
        wtr->WriteLine ("Case #"+(i+1).ToString()+":"+result);
        System::Console::WriteLine ("Case #"+(i+1).ToString()+":"+result);
    }
    rdr->Close();
    wtr->Close();
    return 0;
}

System::String^ RunTest (System::String^ str)
{
    System::String^ retval = "";

    System::Int32 K, C, S;
    array<System::String^>^ strs = str->Split(' ');
    K = System::Convert::ToInt32(strs[0]);
    C = System::Convert::ToInt32(strs[1]);
    S = System::Convert::ToInt32(strs[2]);

    if (S == K)
    {
        if (K==1) retval += " 1";
        else
        {
            System::Int64 max = 1;
            for (System::Int32 i=0; i<C; i++)
            {
                max *= K;
            }
            max--;
            max /= (K-1);
            System::Int64 j=0;
            for (System::Int64 i=1; i<S; i++, j+=max)
            {
                retval += " " + (1+j).ToString();
            }
            retval += " " + (j+1).ToString();
        }
    }
    return retval;
}

System::Int32 Element (System::Int32 c, System::Int32 N, System::Int32 M)
{
    if (c==0) return 1<<N;
    else
    {
        System::Int32 E1 = Element(c-1, N/M, M);
        return (1<<N) | E1;
    }
}