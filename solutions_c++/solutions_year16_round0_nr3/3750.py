#include <iostream>
#include <math.h>
#include <cstdio>

using namespace std;

bool storeVal[51];
bool outputVal[500][51];
long long holdToCommit[500][10];

bool isPrime(unsigned long long n, long long* out)
{
    int i,j,k;
    for(i =2;i<sqrt(n)+1;i++)
    {
        if(n%(unsigned long long)i == 0)
        {
            *(out) = i;
            return false;
        }
    }
    return true;
}

void setBool(int length)
{
    int i;

    for(i=1;i<length-1;i++)
    {
        storeVal[i]=false;
    }

    storeVal[0]=true;
    storeVal[length-1]=true;

}

void increaseBool(int length)
{
    int i=1;
    bool carry = false, toAdd = true;
    for(i=1;i<length;i++)
    {
        if (storeVal[i] == true)
        {
            if(toAdd)
            {
                storeVal[i] = false;
                toAdd = false;
                carry = true;
            }
            else if(carry)
            {
                storeVal[i] = false;
            }
        }
        else
        {
            if(toAdd || carry)
            {
                storeVal[i]=true;
                toAdd = false;
                carry = false;
            }
        }
    }
}

unsigned long long boolToInt(int base,int length)
{
    int i;
    unsigned long long out=0;
    for(i=0;i<length;i++)
    {
        if(storeVal[i] == true)
        {
            out += pow(base,i);
        }
    }
    return out;
}

int main()
{
    int numTestCases;
    int length,numRequired;
    unsigned long long testVal;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>numTestCases;
    cin>>length>>numRequired;

    int i,j,k,successCount,base;

    for(i=0;i<numTestCases;i++)
    {
        if(i!=0)
            cout<<"\n";
        cout<<"Case #"<<i+1<<":\n";

        successCount = 0;
        setBool(length);

        while(successCount<=numRequired)
        {
            for(j=2;j<=10;j++)                   //bases 2 to 9
            {
                testVal = boolToInt(j,length);  //int in that base
                if(!isPrime(testVal,&holdToCommit[successCount][j]))           //if composite, try next base, else try next number
                {
                    continue;
                }
                else
                {
                    break;
                }
            }
            if(j == 11)                         //composite on all bases
            {
                successCount++;                 //these many successes
                for(k=0;k<length;k++)
                {
                    outputVal[successCount-1][k] = storeVal[k];   //store in final array
                }
            }
            increaseBool(length);
        }

    }

    for(int u=0;u<numRequired;u++)
    {
        for(int v=length-1;v>=0;v--)
        {
            cout<<outputVal[u][v];
        }
        for(int v=2;v<=10;v++)
        {
            cout<<" ";
            cout<<holdToCommit[u][v];
        }
        if(u!=numRequired-1)
            cout<<endl;
    }

    return 0;
}
