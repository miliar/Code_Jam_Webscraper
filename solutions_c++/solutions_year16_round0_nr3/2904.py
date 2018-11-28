// C_Coin_Jam.cpp : main project file.

#include "stdafx.h"

using namespace System;

//System::String^ RunTest (System::String^ str);
System::String^ RunTest (System::String^ str, array<System::Int32>^ p);

int main(array<System::String ^> ^args)
{
    System::IO::TextReader^ rdr2 = gcnew System::IO::StreamReader(args[1]);
    System::String^ str;
    array<System::Int32>^ primes = gcnew array<System::Int32>(404);
    System::Int32 cnt = 0;
    while ((str = rdr2->ReadLine()) != nullptr)
    {
        primes[cnt] = System::Convert::ToInt32(str);
        cnt++;
    }
    rdr2->Close();

    System::IO::TextReader^ rdr = gcnew System::IO::StreamReader(args[0]);
    System::String^ outname = args[0]->Substring(0,args[0]->LastIndexOf("."))+".out";
    System::IO::TextWriter^ wtr = gcnew System::IO::StreamWriter(outname);
    System::Int32 NumTests = System::Convert::ToInt32 (rdr->ReadLine());
    for (System::Int32 i=0; i<NumTests; i++)
    {
        wtr->WriteLine ("Case #"+(i+1).ToString()+":");
        System::Console::WriteLine ("Case #"+(i+1).ToString()+":");
        //System::String^ result = RunTest(rdr->ReadLine());
        System::String^ result = RunTest(rdr->ReadLine(), primes);
        wtr->Write (result);
        System::Console::Write (result);
    }
    rdr->Close();
    wtr->Close();
    return 0;
}
System::Int64 Generate (System::Int64 d, System::Int32 b);
//System::Int32 TestFactor(System::Int64 t);
System::Int32 TestFactor(System::Int64 t, array<System::Int32>^ p);

//System::String^ RunTest (System::String^ str)
System::String^ RunTest (System::String^ str, array<System::Int32>^ p)
{
    System::String^ retval = "";
    /* 16 50 */
    System::Int32 sz, num;
    array<System::String^>^ strs = str->Split(' ');
    sz = System::Convert::ToInt32(strs[0]);
    num = System::Convert::ToInt32(strs[1]);
    System::Int32 found = 0;
    System::Int64 basenum;
    basenum = (System::UInt32) (1<<(sz-1));
    basenum |= 1;
    for (System::Int64 i=0; i<(System::Int64) (1<<(sz-2)) && found < num; i++)
    {
        array<System::Int32>^ factor = gcnew array<System::Int32>(9);
        factor->Initialize();
        System::Int32 j;
        System::Int64 testnum;
        for (j=2; j<11; j++)
        {
            testnum = Generate (basenum + (i<<1), j);
            //factor[j-2] = TestFactor(testnum);
            factor[j-2] = TestFactor(testnum, p);
            if (factor[j-2] == 0) break;
        }
        if (j==11)
        {
            found++;
            retval += System::Convert::ToString(basenum + (i<<1), 2);
            for each (System::Int32 f in factor)
            {
                retval += " " + f.ToString();
            }
            retval += System::Environment::NewLine;
        }
    }
    return retval;
}
System::Int64 Generate (System::Int64 d, System::Int32 b)
{
    System::Int64 retval = 0;
    System::Int64 pow = 1;
    for (System::Int32 i=0; i<32; i++)
    {
        if (d&(System::Int64)(1<<i)) retval += pow;
        pow *= b;
    }
    return retval;
}

//System::Int32 TestFactor(System::Int64 t)
System::Int32 TestFactor(System::Int64 t, array<System::Int32>^ p)
{
    //if ((t&1) == 0) return 2;
    //System::Int32 upper = (System::Int32) (System::Math::Sqrt((double) t)/2.) + 1;
    //for (System::Int32 i=1; i<upper; i++)
    //{
    //    if ((t%((i*2)+1)) == 0) return (i*2)+1;
    //}
    System::Int32 upper = p->Length;
    for (System::Int32 i=0; i<upper; i++)
    {
        if (t%p[i] == 0) return p[i];
    }
    return 0;
}