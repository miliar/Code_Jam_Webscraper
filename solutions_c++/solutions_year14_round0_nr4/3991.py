#include <stdio.h>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

#define MyType float

using namespace std;

int compare (const void * a, const void * b)
{
    return *(int*)a-*(int*)b;
}

int compareMyType (const void * b, const void * a)
{
  if ( *(MyType*)a <  *(MyType*)b ) return -1;
  if ( *(MyType*)a == *(MyType*)b ) return 0;
  if ( *(MyType*)a >  *(MyType*)b ) return 1;
}

int main()
{
    ifstream fin("D-large.in");
    int t;
    fin >> t;
    ofstream fout("output.txt");
    for(int s=1; s<=t; ++s)
    {
        int n;
        fin >> n;
        float na[n],ke[n];
        for(int i=0; i<n; ++i)
            fin >> na[i];
        for(int i=0; i<n; ++i)
            fin >> ke[i];

        qsort(na,n,sizeof(float),compareMyType);
        qsort(ke,n,sizeof(float),compareMyType);

        /*printf("naomi\n");
        for(int i=0; i<n; ++i)
            printf("%.6f ",na[i]);
        printf("\n");

        printf("ken\n");
        for(int i=0; i<n; ++i)
            printf("%.6f ",ke[i]);
        printf("\n");*/

        int maxdec=0;
        for(int i=0; i<n; ++i)
        {
            bool flag=1;
            for(int j=0; j<n-i; ++j)
            {
                if(na[j]<ke[j+i])
                {
                    flag=0;
                    break;
                }
            }
            if(flag)
            {
                maxdec=n-i;
                break;
            }
        }
        //printf("dec %d\n",maxdec);

        vector <float> num;
        vector <int> parz;
        //vector <int> tot;
        int tot2,tot3;
        int cn=0;
        int ck=0;
        for(int i=0; i<2*n; ++i)
        {
            if(na[cn]>ke[ck])
            {
                num.push_back(na[cn]);
                parz.push_back(1);
                ++cn;
            }
            else
            {
                num.push_back(ke[ck]);
                parz.push_back(-1);
                ++ck;
            }
        }
        /*for(int i=0; i<2*n; ++i)
        {
            printf("%.6f ",num[i]);
        }
        printf("\n");
        for(int i=0; i<2*n; ++i)
        {
            printf("%d ",parz[i]);
        }
        printf("\n");*/

        /*tot.push_back(parz[0]);
        for(int i=1; i<2*n; ++i)
        {
            if(tot[i-1]>0 && parz[i]<0)
                tot.push_back(parz[i]);
            else
                tot.push_back(tot[i-1]+parz[i]);
        }
        /*for(int i=0; i<2*n; ++i)
        {
            printf("%d ",tot[i]);
        }
        printf("\n");*/

        /*
        tot2=0;
        for(int i=0; i<2*n; ++i)
        {
            if(tot[i]>0)
            ++tot2;
        }*/

        tot3=0;
        for(int i=2*n-1; i>=0; --i)
        {
            tot3+=parz[i];
            if(tot3<0)
                tot3=0;
        }

        //printf("war %d\n",tot2);

        cout << "Case #" << s << ": " << maxdec << " " << tot3 << endl;
        fout << "Case #" << s << ": " << maxdec << " " << tot3 << endl;
        //AAAAAAAAAAAAAAAAAA
        //break;
    }
}
