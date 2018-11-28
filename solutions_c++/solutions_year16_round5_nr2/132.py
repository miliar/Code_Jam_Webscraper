#include<cstdio>
#include<chrono>
#include<algorithm>
#include<vector>
#include<iostream>
#include<string>
#include<cstdlib>
#include<numeric>
using namespace std;
int tc,n,m;
vector<int> postreq[101];
int weights[101];
char coursename[101];
string cool[5];
int injectweights(int index){
    return weights[index]=accumulate(postreq[index].cbegin(),postreq[index].cend(),1,[](const int&sum,const int& el){
        return sum+injectweights(el);
    });
}
int main(){
    srand(123124);
    scanf("%d",&tc);
    for(int ct=1;ct<=tc;++ct){
        scanf("%d",&n);
        for(int i=0;i<=n;++i){
            postreq[i].clear();
        }
        for(int i=1;i<=n;++i){
            int p;
            scanf("%d",&p);
            postreq[p].push_back(i);
        }
        for(int i=1;i<=n;++i){
            scanf(" %c",&coursename[i]);
        }
        coursename[0]='a';
        injectweights(0);
        scanf("%d",&m);
        printf("Case #%d:",ct);
        for(int i=0;i<m;++i){
            cin>>cool[i];
            cool[i]=cool[i];
            long long totalct=0ll;
            long long goodct=0ll;
            chrono::time_point<chrono::system_clock> end_time=chrono::system_clock::now()+chrono::duration<int, milli>(2000/tc);
            //chrono::time_point<chrono::system_clock> end_time=chrono::system_clock::now()+chrono::duration<int, milli>(1000/tc);
            while(chrono::system_clock::now()<end_time){
                vector<int>currcourses;
                currcourses.reserve(101);
                currcourses.push_back(0);
                string res;
                while(currcourses.size()>0){

                    int sumt=accumulate(currcourses.cbegin(),currcourses.cend(),0,[](const int& sum,const int& course){
                        return sum+weights[course];
                    });
                    int ind=rand()%sumt;
                    for(vector<int>::iterator it=currcourses.begin();it!=currcourses.end();++it){
                        if(ind-weights[*it]<0){
                            ind=it-currcourses.begin();
                            break;
                        }
                        ind-=weights[*it];
                    }
                    int cc=currcourses[ind];
                    currcourses.erase(currcourses.begin()+ind);
                    if(coursename[cc]!='a')res.push_back(coursename[cc]);
                    for(vector<int>::const_iterator it=postreq[cc].cbegin();it!=postreq[cc].cend();++it){
                        currcourses.push_back(*it);
                    }
                }
                //cout<<cool[i]<<" "<<res<<endl;
                ++totalct;
                if(res.find(cool[i])!=string::npos){
                    ++goodct;
                    //printf("test");
                }
            }
            cout<<" "<<(double)goodct/totalct;
            //printf(" %lf",((double)goodct)/totalct);
        }
        printf("\n");
    }
}
