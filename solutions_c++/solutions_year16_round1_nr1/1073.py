#include<bits/stdc++.h>
using namespace std;
string S;
deque<char>deq;

int main()
{
       int T,it, i,N;

       freopen("A-large.in","r",stdin);
       freopen("A.out","w",stdout);
       scanf("%d",&T);
       for(it=1; it<=T; it++)
       {
             cin>>S;
             N=S.size();

             while(!deq.empty())  deq.pop_back();
             deq.push_back(S[0]);

             for(i=1; i<N; i++)
            {
                  if(S[i]>=deq.front())
                       deq.push_front(S[i]);
                  else deq.push_back(S[i]);
            }

            printf("Case #%d: ",it);
            while(!deq.empty()){
                 printf("%c",deq.front());
                 deq.pop_front();
            }
            puts("");

       }

      return 0;
}
