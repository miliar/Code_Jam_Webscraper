#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
char a[2050];
int times[26];
vector<int>v;
int Case = 1;
int main(){
    int T;
    #ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("out1.txt", "w", stdout);
    #endif
    scanf("%d\n",&T);
    while(T--){
        v.clear();
        memset(times,0,sizeof(times));
        gets(a);
        for(int i=0;a[i]!='\0';i++)
            times[a[i]-'A']++;
        if(times[25]){
            int c = times[25];
            times[25]-=c;
            times[4]-=c;
            times[17]-=c;
            times[14]-=c;
            while(c--)
                v.push_back(0);
        }
        if(times[22]){
            int c = times[22];
            times[19]-=c;
            times[22]-=c;
            times[14]-=c;
            while(c--)
                v.push_back(2);
        }
        if(times[20]){
            int c = times[20];
            times[5]-=c;
            times[14]-=c;
            times[20]-=c;
            times[17]-=c;
            while(c--)
                v.push_back(4);
        }
        if(times[23]){
            int c = times[23];
            times[18]-=c;
            times[8]-=c;
            times[23]-=c;
            while(c--)
                v.push_back(6);
        }
        if(times[6]){
            int c = times[6];
            times[4]-=c;
            times[8]-=c;
            times[6]-=c;
            times[7]-=c;
            times[19]-=c;
            while(c--)
                v.push_back(8);
        }
        if(times[5]){
            int c = times[5];
            times[5]-=c;
            times[8]-=c;
            times[21]-=c;
            times[4]-=c;
            while(c--)
                v.push_back(5);
        }
        if(times[18]){
            int c = times[18];
            times[18]-=c;
            times[4]-=c;
            times[21]-=c;
            times[4]-=c;
            times[13]-=c;
            while(c--)
                v.push_back(7);
        }
        if(times[19]){
            int c = times[19];
            times[19]-=c;
            times[7]-=c;
            times[17]-=c;
            times[4]-=c;
            times[4]-=c;
            while(c--)
                v.push_back(3);
        }
        if(times[14]){
            int c = times[14];
            times[14]-=c;
            times[13]-=c;
            times[4]-=c;
            while(c--)
                v.push_back(1);
        }
        if(times[8]){
            int c = times[8];
            times[13]-=c;
            times[8]-=c;
            times[13]-=c;
            times[4]-=c;
            while(c--)
                v.push_back(9);
        }
        sort(v.begin(),v.end());
        printf("Case #%d: ",Case++);
        for(int i=0;i<v.size();i++)
            printf("%d",v[i]);
        puts("");
    }
    return 0;
}
