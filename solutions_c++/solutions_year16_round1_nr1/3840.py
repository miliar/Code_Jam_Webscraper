#include<bits/stdc++.h>
using namespace std;
#define read freopen("A-large.in","r",stdin)
#define write freopen("output.txt","w",stdout)

deque<char>dq;
int main(){
//    read;
//    write;
    int T, t=1;
    cin>>T;
    while(T--){
        string str; char start, finish;
        cin>>str;

        for(int i=0; i<str.size(); i++){
            if(i==0){
                start=str[i];
                finish=str[i];
                dq.push_back(str[i]);
            }
            else if(str[i]>=start){
                start=str[i];
                dq.push_front(str[i]);
            }
            else{
                finish=str[i];
                dq.push_back(str[i]);
            }
//            for(deque<char>::iterator it=dq.begin(); it!=dq.end(); it++){
//                printf("%c",*it);
//            }
//            printf("\n");
        }
//        printf("\n\n");
        printf("Case #%d: ", t++);
        for(deque<char>::iterator it=dq.begin(); it!=dq.end(); it++){
            printf("%c",*it);
        }
        printf("\n");

        dq.clear();
    }
    return 0;
}
