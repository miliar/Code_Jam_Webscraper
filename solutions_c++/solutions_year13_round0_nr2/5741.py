#include <iostream>
using namespace std;
int main(){
    int cases;
    cin >> cases;
    for(int casenum=1;casenum <=cases; casenum++){
        int N,M;
        cin >> N >>M; // N rows M colums
        int level[N][M];
        for(int ii=0; ii<N; ii++){
            for(int kk=0; kk<M;kk++){
                cin >> level[ii][kk];
//                  cout<< level[ii][kk] <<" ";
            }
//            cout<<endl;
         }
        int initlev=2;
        bool yesflag=true;
        bool cond1=true, cond2=true;
        for(int ii=0; ii<N; ii++){        
            if(!yesflag) break;
            for(int kk=0; kk<M;kk++){ 
            cond1=true; cond2=true;
                if(level[ii][kk]<initlev &&( level[ii][kk] != level[0][kk] || level[ii][kk] != level[N-1][kk])) cond1=false;

                if(level[ii][kk]<initlev &&(level[ii][kk]!=level[ii][0] || level[ii][kk] != level[ii][M-1])) cond2=false;             
  //      cout<<"(i,k) =("<<ii<<","<<kk<<") (cond1,cond2)=("<<cond1<<","<<cond2<<")"<<endl;
                if(!cond1 & !cond2) {yesflag=false; break; }
                if(level[ii][kk]<initlev && cond1 && !cond2){
                   for(int ll=0;ll<N;ll++) 
                       if(level[ii][kk]!=level[ll][kk]){yesflag=false; break;}
                }
                else if(level[ii][kk]<initlev && cond2 && !cond1){
                   for(int ll=0;ll<M;ll++) 
                       if(level[ii][kk]!=level[ii][ll]){yesflag=false; break;}
                }
          
    //         cout<<"(i,k) =("<<ii<<","<<kk<<") (yesflag)=("<<yesflag<<")"<<endl;

            if(!yesflag) break;
            } 
        }
    
        if(yesflag)
             cout<<"Case #"<<casenum<<": YES"<<endl;
         else
             cout<<"Case #"<<casenum<<": NO"<<endl;
    }

}
