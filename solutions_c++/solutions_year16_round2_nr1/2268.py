#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
char s[3000];
int letter[26];
int num[10];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int k = 1; k <= t; k++)
    {
        cin>>s;
        memset(letter,0,sizeof letter);
        memset(num,0,sizeof num);

        int l = strlen(s);
        for (int i = 0; i < l; i++)
            letter[s[i] - 'A']++;

        num[0] = letter['Z'-'A'];
        num[4] = letter['U'-'A'];
        num[3] = letter['R'-'A'] - num[4] - num[0];
        num[8] = letter['G'-'A'];
        num[2] = letter['T'-'A'] - num[8] - num[3];
//        cout<<letter['T'-'A']<<" "<<num[8]<<" "<<num[3]<<endl;
//        cout<<num[2]<<endl;
        num[5] = letter['F'-'A'] - num[4];
        num[7] = letter['V'-'A'] - num[5];
        num[6] = letter['S'-'A'] - num[7];
        num[1] = letter['O'-'A'] - num[0] - num[2] - num[4];
        num[9] = letter['N'-'A'] - num[1] - num[7];
        num[9] /= 2;
        cout<<"Case #"<<k<<": ";
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < num[i]; j++)
                cout<<i;
        }
        cout<<endl;
    }
    fclose(stdin);
    fclose(stdout);

}
