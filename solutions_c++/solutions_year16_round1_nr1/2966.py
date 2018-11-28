#include <cstdio>
#include <deque>
#include <string>
using namespace std;
char buf[1111]={};
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _tc = 1 ; _tc <= tc ; _tc++ ) {
        printf("Case #%d: ",_tc);
        scanf("%s",buf);
        deque<char> dq;
        dq.push_front(buf[0]);
        for ( int i = 1 ; buf[i] ; i++ ) {
            if ( dq.front() <= buf[i] ) 
                dq.push_front(buf[i]);
            else dq.push_back(buf[i]);
        }
        for ( int i = 0 ; i <(int)dq.size();i++ ) 
            printf("%c",dq[i]);
        puts("");
    }
    return 0;
}
