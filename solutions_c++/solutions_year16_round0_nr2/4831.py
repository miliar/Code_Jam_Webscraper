class Solution {
public:
    string minWindow(string s, string t) {
        int n = s.size();
        vector < map<char,int> > F(n+1);
        
        map<char, int> M;
        for (int i=0;i<t.size();i++) ++M[t[i]];
        
        
        for (int i=0;i<n;i++){
            if (M.find(s[i])!=M.end()){
                for (auto it = M.begin(); it!=M.end(); it++){
                    if (it->first==s[i]) F[i+1][s[i]]= 1 + F[i][s[i]];
                    else F[i+1][s[i]] = F[i][s[i]];
                }
            }
        }
        
        
        int len = n + 3;
        int start = -1;
        for (int i=0;i<n;i++){
            if (M.find(s[i])!=M.end()){
                int flag = 1;
                int idx = n;
                int f = 1;
                int mx = -1;
                for (auto it = M.begin(); it!=M.end(); it++){
                    int reqd = it->second + F[i+1][it->first] + (it->first==s[i]?-1:0);
                    cout<<i<<" "<<(it->first)<<" "<<reqd<<"\n";
                    int lf,rt;
                    lf=i+1, rt=n;
                    while(lf<rt){
                        int mid = (lf + rt)/2;
                        if (F[mid][it->first] >= reqd){
                            f=1;
                            idx=mid;
                            rt=mid-1;
                        }
                        else 
                            lf=mid+1;
                    }
                    flag = flag && f;
                    if (f) mx=max(mx, idx);
                }
                if (f){
                    cout<<start<<" "<<mx<<"\n";
                    if (mx - i + 1 < len){
                        len = mx - i + 1;
                        start = i;
                    }
                }
            }
        }
        if (start<0) return "";
        else{
            string ans = s.substr(start, len);
            return ans;
        }
    }
};