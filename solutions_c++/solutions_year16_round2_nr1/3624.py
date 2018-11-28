#include<iostream>
#include<fstream>
#include<map>
#include<stdlib.h>
#include<string.h>
#include<vector>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("ans.txt");
    int t,j,len,i,count[11],cha[26];
    char s[1111];
    fin>>t;
    for(j=1;j<=t;j++)
    {
        fin>>s;
        len=strlen(s);
        memset(count,0,sizeof(count));
        memset(cha,0,sizeof(cha));
        fout<<"Case #"<<j<<": ";

        for(i=0;i<len;i++)
        {
            cha[s[i]-65]++;
            if(s[i]=='Z')
            {
                count[0]++;
                cha['Z'-65]--;
                cha['E'-65]--;
                cha['R'-65]--;
                cha['O'-65]--;

            }
            if(s[i]=='W')
            {
                count[2]++;
                cha['T'-65]--;
                cha['W'-65]--;
                cha['O'-65]--;

            }
            if(s[i]=='X')
            {
                count[6]++;
                cha['S'-65]--;
                cha['I'-65]--;
                cha['X'-65]--;

            }


            if(s[i]=='G')
            {
                count[8]++;
                cha['E'-65]--;
                cha['I'-65]--;
                cha['G'-65]--;
                cha['H'-65]--;
                cha['T'-65]--;

            }
        }
        if(cha['S'-65]>0)
        {
            count[7]=cha['S'-65];
            cha['E'-65]-=2*cha['S'-65];
            cha['V'-65]-=cha['S'-65];
            cha['N'-65]-=cha['S'-65];
        }

        if(cha['T'-65]>0)
        {
            count[3]=cha['T'-65];
            cha['R'-65]-=cha['T'-65];
            cha['H'-65]-=cha['T'-65];
            cha['E'-65]-=2*cha['T'-65];
        }
        if(cha['R'-65]>0)
        {
            count[4]=cha['R'-65];
            cha['F'-65]-=cha['R'-65];
            cha['O'-65]-=cha['R'-65];
            cha['U'-65]-=cha['R'-65];
        }
        if(cha['F'-65]>0)
        {
            count[5]=cha['F'-65];
            cha['I'-65]-=cha['F'-65];
            cha['V'-65]-=cha['F'-65];
            cha['E'-65]-=cha['F'-65];

        }
        if(cha['O'-65]>0)
        {
            count[1]=cha['O'-65];
            cha['N'-65]-=cha['O'-65];
            cha['E'-65]-=cha['O'-65];

        }
        if(cha['N'-65]>0)
        count[9]=cha['N'-65]/2;
        for(i=0;i<=9;i++)
        {
          //  cout<<count[i]<<" ";
            if(count[i]>0)
            {
                    while(count[i]>0)
                    {
                        fout<<i;
                        count[i]--;
                    }
            }

        }
        fout<<endl;
    }

    return 0;
}
