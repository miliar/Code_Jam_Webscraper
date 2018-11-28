#include<fstream>
#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;

int main()
{
    ifstream fin("A.in");
    ofstream fout("out.txt");
    int t;
    fin>>t;
    for(int pp=0;pp<t;pp++)
    {
        int n;
        fin>>n;
        char c;
        fin.get(c);
        char str1[200],str2[200];
        fin>>str1>>str2;
        cout<<str1<<" "<<str2<<endl;
        int flag = 0 ,ans = 0;
        int i=0,j=0;
        while(i<strlen(str1) && j<strlen(str2))
        {
            char c1 = str1[i];
            char c2 = str2[j];
            if(c1!=c2)
            {
                flag = 1;break;
            }
            else
            {
                int count1=0,count2=0;
                while(i<strlen(str1) && str1[i] == c1)
                {
                    count1++;
                    i++;
                }
                while(j<strlen(str2) && str2[j] == c2)
                {
                    count2++;
                    j++;
                }

                ans += abs(count2-count1);
            }
        }
        if(i<strlen(str1) || j<strlen(str2))
            flag = 1;
        fout<<"Case #"<<pp+1<<": ";
        if(flag)
            fout<<"Fegla Won"<<endl;
        else
            fout<<ans<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
