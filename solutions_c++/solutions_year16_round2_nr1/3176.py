#include <bits/stdc++.h>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

bool arrayNotNull(int a[26])
{
    bool flag=true;

    for(int i=0;i<26;i++)
    {
        if(a[i]>0)
        {
            flag=false;
            break;
        }
    }
    return flag;
}

int main()
{
    int test;
    fin>>test;
    for(int x=1;x<=test;x++)
    {
        char s[2001];
        fin>>s;
        int a[26]={0};
        int b[10]={0};
        int len=strlen(s);

        for(int i=0;i<len;i++)
        {
            int z=(int)s[i]-(int)('A');
            a[z]++;
        }

            while(a[25]>0 && a[4]>0 && a[17]>0 && a[14]>0)
            {
                b[0]++;
                a[25]--;
                a[4]--;
                a[17]--;
                a[14]--;
            }

            while(a[18]>0 && a[8]>0 && a[23]>0)
            {
                a[18]--;
                a[8]--;
                a[23]--;
                b[6]++;
            }

            while(a[5]>0 && a[14]>0 && a[20]>0 && a[17]>0)
            {
                a[5]--;
                a[14]--;
                a[20]--;
                a[17]--;
                b[4]++;
            }

            while(a[19]>0 && a[22]>0 && a[14]>0)
            {
                a[19]--;
                a[22]--;
                a[14]--;
                b[2]++;
            }

            while(a[14]>0 && a[13]>0 && a[4]>0)
            {
                a[14]--;
                a[13]--;
                a[4]--;
                b[1]++;
            }

            while(a[4]>0 && a[8]>0 && a[6]>0 && a[7]>0 && a[19]>0)
            {
                a[4]--;
                a[8]--;
                a[6]--;
                a[7]--;
                a[19]--;
                b[8]++;
            }


            while(a[18]>0 && a[4]>1 && a[21]>0 && a[13]>0)
            {
                a[18]--;
                a[4]--;
                a[21]--;
                a[4]--;
                a[13]--;
                b[7]++;
            }
            while(a[5]>0 && a[8]>0 && a[21]>0 && a[4]>0)
            {
                a[5]--;
                a[8]--;
                a[21]--;
                a[4]--;
                b[5]++;
            }

            while(a[19]>0 && a[7]>0 && a[17]>0 && a[4]>1)
            {
                a[19]--;
                a[7]--;
                a[17]--;
                a[4]--;
                a[4]--;
                b[3]++;
            }

            while(a[13]>1 && a[8]>0 && a[4]>0)
            {
                a[13]--;
                a[8]--;
                a[13]--;
                a[4]--;
                b[9]++;
            }

        fout<<"Case #"<<x<<": ";
        for(int l=0;l<10;l++)
        {
            while(b[l]>0)
            {
                fout<<l;
                b[l]--;
            }
        }
        fout<<endl;
    }


    return 0;
}
