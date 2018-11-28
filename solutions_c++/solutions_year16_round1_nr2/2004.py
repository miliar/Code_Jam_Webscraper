
#include<iostream>
#include<stdio.h>
#include<list>
#include<string.h>
#include<set>

using namespace std;

int main(){
    freopen("B-large (1).in","r",stdin);
	freopen("B-large (1).out","w",stdout);
    int T;
	scanf("%d",&T);
	getchar();
	int x=1;
	set<int>out;
	while(x<=T){
        int N;
        scanf("%d",&N);
        //getchar();
        int n=2*N-1;
        while(n--){
            int s;
            for(int i=0;i<N;i++){
                scanf("%d",&s);
                if(out.empty())
                    out.insert(s);
                else if(out.find(s)!=out.end())
                    out.erase(s);
                else out.insert(s);
            }
            //getchar();
        }
        printf("Case #%d: ",x);
        set<int>::iterator set_it=out.begin();
        while(set_it!=out.end()){
            printf("%d ",*set_it);
            set_it++;
        }
        printf("\n");
        out.clear();
        x++;
	}
}
