#include <iostream>
#include <cstdio>
#include <cstring>
#include <stack>
#include <queue>

using namespace std;

int main()
{
    int T=0;
    char c;
    stack<char> st;
    cin >> T;
    char S[101];

    for(int i=1;i<=T;i++)
    {
        int re=0;
        int lastminus=-1; 
        scanf("%s",S);
        int finish=0;
        while(true){
            int cnt=0;
            lastminus=-1;
            for(int j=strlen(S)-finish-1;j>-1;j--)
            {
                if(S[j]=='-'){
                    lastminus=j;
                    break;
                }
                cnt++;
            }
            finish+=cnt;

            if(lastminus==-1)
                break;
            for(int j=0;j<strlen(S)-finish;j++)
            {
                st.push(S[j]);
            }
            for(int j=strlen(S)-finish-1;j>-1;j--)
            {
                if(st.top()=='-')
                    S[j]='+'; 
                else
                    S[j]='-'; 
                st.pop();
            }
            re++;
        }
        printf("Case #%d: ",i);
        printf("%d\n", re);
    }

    return 0;
}
