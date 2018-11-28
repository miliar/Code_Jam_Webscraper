//Author DBug<Deepak Sharma>
#include <bits/stdc++.h>

#define forn(i,n) for(long int i=0;i<n;i++)
#define fora(i,a,b) for(long int i=a;i<b;i++)
#define vi(v,n) for(int ii=0;ii<n;ii++){int tmpi; cin>>tmpi;v.push_back(tmpi);}
#define vo(v) for(int io=0;io<v.size();io++){cout<<v[io]<<",";}cout<<endl;
#define td(at,bt) cout<<at<<","<<bt<<endl;
#define pb push_back

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	ifstream fin;
	fin.open("input.in");
	ofstream fout;
	fout.open("output.txt");
	int t;
	fin>>t;
	forn(it,t){
	    //cout<<"doing "<<it<<endl;
        vector<int> v(26,0);
        vector<int> res(10,0);
        string s;
        fin>>s;
        //cout<<s<<endl;
        forn(i,s.size()){
            v[int(s[i])-int('A')]++;
        }
        int found=0;int tmp=0;
        while(found!=s.size()){
            while(v[int('Z')-int('A')]>0 && v[int('E')-int('A')]>0 && v[int('R')-int('A')]>0 && v[int('O')-int('A')]>0){
                found+=4;
                v[int('Z')-int('A')]--;
                v[int('E')-int('A')]--;
                v[int('R')-int('A')]--;
                v[int('O')-int('A')]--;
                res[0]++;
            }

            while(v[int('T')-int('A')]>0 && v[int('W')-int('A')]>0 && v[int('O')-int('A')]>0){
                found+=3;
                v[int('T')-int('A')]--;
                v[int('W')-int('A')]--;
                v[int('O')-int('A')]--;
                res[2]++;
            }

            while(v[int('F')-int('A')]>0 && v[int('O')-int('A')]>0 && v[int('U')-int('A')]>0 && v[int('R')-int('A')]>0){
                found+=4;
                v[int('F')-int('A')]--;
                v[int('O')-int('A')]--;
                v[int('U')-int('A')]--;
                v[int('R')-int('A')]--;
                res[4]++;
            }
            while(v[int('F')-int('A')]>0 && v[int('I')-int('A')]>0 && v[int('V')-int('A')]>0 && v[int('E')-int('A')]>0){
                found+=4;
                v[int('F')-int('A')]--;
                v[int('I')-int('A')]--;
                v[int('V')-int('A')]--;
                v[int('E')-int('A')]--;
                res[5]++;
            }
            while(v[int('S')-int('A')]>0 && v[int('I')-int('A')]>0 && v[int('X')-int('A')]>0){
                found+=3;
                v[int('S')-int('A')]--;
                v[int('I')-int('A')]--;
                v[int('X')-int('A')]--;
                res[6]++;
            }
            while(v[int('S')-int('A')]>0 && v[int('V')-int('A')]>0 && v[int('N')-int('A')]>0 && v[int('E')-int('A')]>1){
                found+=5;
                v[int('S')-int('A')]--;
                v[int('V')-int('A')]--;
                v[int('E')-int('A')]-=2;
                v[int('N')-int('A')]--;
                res[7]++;
            }
            while(v[int('E')-int('A')]>0 && v[int('I')-int('A')]>0 && v[int('G')-int('A')]>0 && v[int('H')-int('A')]>0 && v[int('T')-int('A')]>0){
                found+=5;
                v[int('E')-int('A')]--;
                v[int('I')-int('A')]--;
                v[int('G')-int('A')]--;
                v[int('H')-int('A')]--;
                v[int('T')-int('A')]--;
                res[8]++;
            }
            while(v[int('T')-int('A')]>0 && v[int('H')-int('A')]>0 && v[int('R')-int('A')]>0 && v[int('E')-int('A')]>1){
                found+=5;
                v[int('T')-int('A')]--;
                v[int('H')-int('A')]--;
                v[int('E')-int('A')]-=2;
                v[int('R')-int('A')]--;
                res[3]++;
            }
           while(v[int('N')-int('A')]>1 && v[int('I')-int('A')]>0 && v[int('E')-int('A')]>0){
                found+=4;
                v[int('N')-int('A')]-=2;
                v[int('I')-int('A')]--;
                v[int('E')-int('A')]--;
                res[9]++;
            }
            while(v[int('O')-int('A')]>0 && v[int('N')-int('A')]>0 && v[int('E')-int('A')]>0){
                found+=3;
                v[int('O')-int('A')]--;
                v[int('N')-int('A')]--;
                v[int('E')-int('A')]--;
                res[1]++;
            }
            //vo(res);
            //cout<<found<<endl;
            //if(tmp>10) break;
            //tmp++;
        }
		if(it==0){
			fout<<"Case #"<<it+1<<": ";
			forn(i,10){
                while(res[i]!=0){
                    fout<<i;
                    res[i]--;
                }
            }
		}
		else{
			fout<<endl<<"Case #"<<it+1<<": ";
			forn(i,10){
                while(res[i]!=0){
                    fout<<i;
                    res[i]--;
                }
            }
		}
	}
}

