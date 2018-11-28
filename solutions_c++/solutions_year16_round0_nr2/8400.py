#include"cstdio"
#include"iostream"
#include"map"
#include"string"
#include"cstring"
#include"vector"
#include"utility"
#include"algorithm"
#include"cmath"
#include"queue"
#include"stack"
#include"set"

using namespace std;
#define visMax 2016
class solution{
    public:
        int vis[visMax];
        int string2int(const string&cakestat){
            int ret(0);
            for(int i = 0;i<cakestat.size();i++){
                ret<<=1;
                if(cakestat[i]=='+')ret+=1;
            }
            return ret;
        }
        bool isok(const string& cakestat){
            for(auto it = cakestat.begin();it!=cakestat.end();it++)if((*it)=='-')return false;
            return true;
        }
        string flip(int pos,const string&cakestat){
            int N = cakestat.size();
            if(pos>=N) return cakestat;
            string ret;
            for(int i = pos;i>=0;i--){
                if(cakestat[i]=='+')ret.push_back('-');
                else ret.push_back('+');
            }
            ret+=cakestat.substr(pos+1,N-pos-1);
            return ret;

        }
        int solve(const string& cakes){
            memset(vis,0,sizeof(vis));
            queue<string>curline;
            if(isok(cakes))return 0;
            curline.push(cakes);
            vis[string2int(cakes)] = 1;
            int ret = 0;
            int N = cakes.size();
            int curlen = 1;
            while(curline.empty()==false){
                ret++;
                int nxtlen = 0;
                while(curlen-->0){
                    string curcake = curline.front();
                    curline.pop();
                    for(int i = 0;i<N;i++){
                        string nxtcake = flip(i,curcake);
                        if(vis[string2int(nxtcake)]==0){
                            vis[string2int(nxtcake)] = 1;
                            if(isok(nxtcake)==true)return ret;
                            curline.push(nxtcake);
                            nxtlen++;
                        }
                    }
                }
                curlen = nxtlen;
            }
            return -1;
        }
};
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
	int T;
	int casenum=0;
	cin>>T;
    solution sol;
	while(casenum++<T){
        string cakes;
        cin>>cakes;
        int res(-1);
        res = sol.solve(cakes);
        printf("Case #%d: %d\n",casenum,res);
	}


return 0;}
