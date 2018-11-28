//
//  fairsqbig.cpp
//  
//
//  Created by Abdallah on 4/13/13.
//
//

#include <fstream>
#include <iostream>

using namespace std;

bool pel(long long x)
{
    long long temp=x;
    long long mafkok[100];
    int dig=1,i;
    for(i=0;;i++)
    {
        mafkok[i]=temp%10;
        temp=temp/10;
        if(temp==0)
            break;
        dig++;
    }
    
    for(i=0;i<dig/2;i++)
    {
        if(mafkok[i]!=mafkok[dig-i-1])
            return false;
    }
    return true;
}

main()
{
    ifstream fin;
    ofstream fout;
    
    long long fairsq[1000000];
    fairsq[0]=1; fairsq[1]=4; fairsq[2]=9;
    int countfs=3;
    
    long long i,j;
    for(i=11;i<10000000;i++)
    {
        if(pel(i)&&pel(i*i))
        {
            fairsq[countfs]=i*i;
            countfs++;
        }
    }
    cout<<countfs<<endl;
    for(i=0;i<countfs;i++)
        cout<<fairsq[i]<<endl;
    
    fin.open("data.in.txt");
    fout.open("data.out.txt");
    
    int T;
    long long A,B;
    fin>>T;
    
    for(i=0;i<T;i++)
    {
        fin>>A>>B;
        int C=0;
        for(j=0;j<countfs;j++)
        {
            if(fairsq[j]>=A && fairsq[j]<=B)
                C++;
        }
        fout<<"Case #"<<i+1<<": "<<C<<endl;
    }
    fin.close();
    fout.close();
}