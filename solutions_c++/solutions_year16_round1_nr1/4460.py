#include<cstdio>
#include<deque>
using namespace std;
char str[2000],out[2000];
int main()
{
    int t,s,i,j,k,l;
    deque<char> deq;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%s",str);
        deq.clear();
        for(j=0;str[j]!='\0';j++){
            for(k=0;k<deq.size();k++){
                if(str[j]==deq[k])
                    continue;
                break;
            }
            if(k==deq.size()){
                deq.push_back(str[j]);
            }
            else{
                if(deq[k]>str[j])
                    deq.push_back(str[j]);
                else
                    deq.push_front(str[j]);
            }
        }
        for(j=0;j<deq.size();j++){
            out[j]=deq[j];
        }
        out[j]='\0';
        printf("Case #%d: %s\n",i,out);
    }
    return 0;
}
