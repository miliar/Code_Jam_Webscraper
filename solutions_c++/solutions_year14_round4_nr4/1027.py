#include<iostream>
#include<vector>
#include<string>
#include<map>
using namespace std;

vector<string> arr;
vector<int> st[15],cnt;
int M,N;

int calc(vector<int>& tar,int idx)
{
       map<string,bool> m;
       int CNT = cnt[idx];
       for(int i = 0 ; i < CNT; i++)
               for(int j = 0 ; j <= arr[tar[i]].size(); j++)
               {
                     m[arr[tar[i]].substr(0,j)] = 1;  
               }
       return m.size();
}

pair<int,int> sol(int idx)
{
    if(idx == arr.size())
    {
           int ans = 0;
           for(int i = 0 ; i < N; i++)
                   ans += calc(st[i],i);
           return make_pair(ans,1);       
    }
    pair<int,int> ans((int)-1e9,1);
    for(int i = 0 ; i < N; i++)
    {
             // cout << idx << " " << cnt[i] << endl;
            if(cnt[i] + 1 > st[i].size())
                      st[i].push_back(idx);
            else
                      st[i][cnt[i]] = idx;
            cnt[i]++;
            pair<int,int> res = sol(idx + 1);
            if(res.first > ans.first)
                         ans = res;
            else if(res.first == ans.first)
                         ans = make_pair(ans.first,res.second + ans.second);
            cnt[i]--;
    }
    return ans;
}


int main()
{
    
    freopen("in22.in","r",stdin);
    freopen("out.out","w",stdout);
    int T,TEST = 1;
    cin >> T;
    while(T--)
    {
              cerr << TEST << endl;
        cin >> M >> N;
        arr.clear();cnt.clear();
        arr.resize(M);
        for(int i = 0 ; i < M; i++)
                cin >> arr[i];
             
        cnt.resize(N);    
        pair<int,int> ans = sol(0);
        cout << "Case #"<<TEST++<<": " << ans.first << " " << ans.second << endl;      
    }   
}
