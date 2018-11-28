#include<iostream>
#include<math.h>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
    char s1[110],s2[110];
    int i,j,n,t,k;

    cin >> t;

    for(k=1;k<=t;k++)
    {

    cin >> n;

    scanf("%s",s1);
    scanf("%s",s2);

    if( !strcmp(s1,s2) )
    {
        cout << "Case #" << k <<": 0\n";
        continue;
    }

    int bit = 1;

    int n1  = strlen(s1);
    int n2  = strlen(s2);


    int moves =  0;

    int h1[26] = {0};
    int h2[26] = {0};

    for(i=0;i<n1;i++)
            h1[s1[i]-'a'] ++;

    for(i=0;i<n2;i++)
            h2[s2[i]-'a'] ++;

    for(i=0;i<26;i++)
    {
        if( (!h1[i] && h2[i]) || (h1[i] && !h2[i]) )
            bit = 0;
    }

    i = 0;
    j = 0;

    moves = 0;
    while( i < n1 )
    {
        int t1 = 0, t2 = 0;
        char tmp = s1[i];
        if( j >= n2 )
        {
            bit = 0;
            break;
        }
        while( i<n1 && s1[i] == tmp){ i++; t1++; }
        while( j<n2 && s2[j] == tmp){ j++; t2++; }

        if( t2 == 0 )
        {
            bit = 0;
            break;
        }

        if(t1 > t2) moves += t1 - t2;
        else moves += t2 - t1;
    }

    if( j!=n2 )
        bit = 0;

    if( !bit )
    {
        cout << "Case #" << k <<": Fegla Won\n";
        continue;
    }
    cout << "Case #"<< k <<": "<< moves << endl;
    }
}
