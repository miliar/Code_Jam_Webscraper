#include<set>
#include<vector>
#include<iostream>
#include<algorithm>

using namespace std; 

typedef set<double>::iterator Iter; 
typedef set<double>::reverse_iterator RIter; 

int game1(set<double> & s1, set<double> & s2){
    int re = 0; 
    int n = s1.size(); 
    for(Iter pos = s1.begin(); pos != s1.end(); ++pos){
        double d = *pos; 
        double d1 = *s2.rbegin();    
        double d2 = *s2.begin();
        if(d > d2){
            re++; 
            s2.erase(s2.begin());
        }else if(d < d2){
            Iter pos1 = s2.end(); 
            --pos1; 
            s2.erase(pos1); 
        }
    }

    return re;
}

int game2(set<double> &s1, set<double> &s2){
    int re = 0; 
    int n = s1.size(); 
    Iter p1 = s2.begin();
    for(Iter pos = s1.begin(); pos != s1.end(); ++pos){
        double d = *pos; 
        while(p1 != s2.end() && *p1 < d)
            ++p1; 
        if(p1 == s2.end())
            break; 
        else {
            ++p1; 
            ++re;
        }
    }
    return n-re;
}

int main(){
    int T; 
    cin >> T; 
    for(int t = 1; t <= T; t++){
        int n ; 
        set<double> v1,v2; 
        cin >> n ; 
        for(int i = 0; i < n; i ++){
            double temp ; 
            cin >> temp ; 
            v1.insert(temp); 
        }
        for(int i = 0; i < n; i ++){
            double temp ; 
            cin >> temp ; 
            v2.insert(temp); 
        }
        cout << "Case #" << t << ": " << game1(v1,v2) << " " << game2(v1,v2) << endl; 
    }
}
