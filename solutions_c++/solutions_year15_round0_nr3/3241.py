#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)

int mult(int a,int b){
    int res[][4]={
        {1,2,3,4},
        {2,-1,4,-3},
        {3,-4,-1,2},
        {4,3,-2,-1}
    };
    if(a*b>0) return res[abs(a)-1][abs(b)-1];
    else return -res[abs(a)-1][abs(b)-1];
}

int cvt(char c){
    if(c=='i') return 2;
    if(c=='j') return 3;
    if(c=='k') return 4;
}

int main(){
	int T;
    cin >> T;
    REP(t,T){
        cout << "Case #" << t+1 << ": ";
        int x,l,n;
        string ss,s;
        cin >> l >> x >> ss;
        REP(i,x) s+=ss;
        n=l*x;
        
        int ni=1;
        int pos=0;
        for(;pos<n;pos++){
            ni=mult(ni,cvt(s[pos]));
            if(ni==2) break;
        }
        pos++;
        //cout << pos << " ";
        if(pos>=n){
            cout << "NO" << endl;
            continue;
        }

        int nk=1;
        int pos2=n-1;
        for(;pos2>=0;pos2--){
            nk=mult(cvt(s[pos2]),nk);
            if(nk==4) break;
        }
        pos2--;
        //cout << pos2 << " ";
        if(pos2<0){
            cout << "NO" << endl;
            continue;
        }
        
        int nj=1;
        for(int j=pos;j<=pos2;j++){
            nj=mult(nj,cvt(s[j]));
        }
        if(nj==3) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    /*
    REP(i,4){
        REP(j,4) cout << mult(i+1,j+1) << " ";
        cout << endl;
    }
    */
	return 0;
}

