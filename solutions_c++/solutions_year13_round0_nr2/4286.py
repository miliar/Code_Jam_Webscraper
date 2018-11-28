using namespace std;
#include <iostream>
#include <map>
#include <vector>
void disp(vector<vector<int> > F) {
    cout<<"F:\n"; int y,z;
    for(y=0;y<F.size();y++) {
        for(z=0;z<F[y].size();z++)
            cout<<F[y][z]<<" ";
        cout<<endl;
    }
}
void clearR(vector<vector<int> > &F,vector<int> R) {
    int x;
    for(x=R.size()-1;x>=0;x--) {
        F.erase(F.begin()+R[x]);
    }
}
bool clearC(vector<vector<int> > &F,vector<int> C) {
    int x,z;
    for(x=C.size()-1;x>=0;x--) {
        for(z=0;z<F.size();z++) {
            F[z].erase(F[z].begin()+C[x]);
        }
    }
    if(F.size()) {
        if(F[0].size()==0)
            F.clear();
    }
}
int small(vector<vector<int> > &F, vector<int> &R, vector<int> &C) {
    int x,y,s;
    map <int,bool> D,Rm,Cm;
    for(x=0;x<F.size();x++) {
        for(y=0;y<F[x].size();y++) {
            if(x==0 && y==0) {
                Rm[x]=1; Cm[y]=1;
                R.push_back(x);
                C.push_back(y);
                s=F[x][y];
            } else {
                if (s==F[x][y]) {
                    if(Rm[x]==0) {
                        Rm[x]=1;
                        R.push_back(x);
                    }
                    if(Cm[y]==0) {
                        Cm[y]=1;
                        C.push_back(y);
                    }
                } else if (F[x][y]<s) {
                    Cm=D; Rm=D; R.clear(); C.clear();
                    Rm[x]=1; Cm[y]=1;
                    R.push_back(x);
                    C.push_back(y);
                    s=F[x][y];
                }
            }
        }
    }
    sort(R.begin(),R.end()); sort(C.begin(),C.end());
    return s;
}
void common(vector<vector<int> > F, map<int,bool> &R, map<int,bool> &C) {
    int x,y,s;
    for(x=0;x<F.size();x++) {
        bool f=true; 
        for(y=0;y<F[x].size();y++) {
            if(y==0)
                s=F[x][y];
            else {
                if(s!=F[x][y]) {
                    f=false;
                    break;
                }
            }
        }
        R[x]=f;
    }
    if (F.size()) {
    for(x=0;x<F[0].size();x++) {
        bool f=true;
        for(y=0;y<F.size();y++) {
            if(y==0)
                s=F[y][x];
            else {
                if(s!=F[y][x]) {
                    f=false;
                    break;
                }
            }
        }
        C[x]=f;
    }
    }
}
int main() {
	int T,x,y,z,M,N,s;
	cin>>T;
	for(x=0;x<T;x++) {
		cin>>N>>M;
		vector<int> A(M,-1);
        vector<vector<int> > F(N,A);
		for(y=0;y<N;y++) {
			for(z=0;z<M;z++)
				cin>>F[y][z];
		}
        bool P=true;
        while(F.size()) {
            vector<int> Rs,Cs;
            s=small(F,Rs,Cs);
            //cout<<"Rs "; for(y=0;y<Rs.size();y++) cout<<Rs[y]<<" "; cout<<endl;
            //cout<<"Cs "; for(y=0;y<Cs.size();y++) cout<<Cs[y]<<" "; cout<<endl;
            map<int,bool> Rc,Cc;
            common(F,Rc,Cc); 
            //cout<<"Rc "; for(y=0;y<F.size();y++)  if(Rc[y]==1) cout<<y<<" ";  cout<<endl;
            //if(F.size()) { cout<<"Cc "; for(y=0;y<F[0].size();y++)  if(Cc[y]==1) cout<<y<<" ";  cout<<endl; }
            bool Rf = false, Cf = false;
            for(y=0;y<Rs.size();y++) {
                if(Rc[Rs[y]]==0) {
                    Rs.erase(Rs.begin()+y);
                    y--;
                } else {
                    Rf = true;
                }
            }
            for(y=0;y<Cs.size();y++) {
                if(Cc[Cs[y]]==0) {
                    Cs.erase(Cs.begin()+y);
                    y--;
                } else {
                    Cf = true;
                }
            }
            if (Rf==false && Cf==false) {
                P=false;
                break;
            }
            //cout<<"Rs "; for(y=0;y<Rs.size();y++) cout<<Rs[y]<<" "; cout<<endl;
            //cout<<"Cs "; for(y=0;y<Cs.size();y++) cout<<Cs[y]<<" "; cout<<endl;
            if(Rf) clearR(F,Rs);
            //cout<<"Clear R\n"; disp(F);
            if(Cf) clearC(F,Cs);
            //cout<<"Clear C\n"; disp(F);
        }
        cout<<"Case #"<<x+1<<": ";
		if(P) cout<<"YES\n";
		else cout<<"NO\n";
	}
	return 0;
}
