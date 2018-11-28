#include<cstdio>
#include<fstream>
#include<vector>
#include<string>
#include<cmath>
using namespace std;
vector<string> words;
vector< pair<int, int> > parse[101];
int T,N;
int main(){
    
    ifstream fin;
    ofstream fout;
    fin.open("inputA2.in");
    fout.open("outputA.txt");
    
    fin>>T;
    for(int i=1;i<=T;++i){
        bool win = true;
        fin>>N;
        //printf("T: %d N: %d\n",i,N);
        string tmp;
        getline(fin, tmp);
        words = vector<string>();
        for(int w=0;w<N;++w){
            parse[w] = vector< pair<int, int> >();
        }
        for(int j=0;j<N;++j){
            getline(fin, tmp);
            //printf("%s\n",tmp.c_str());
            words.push_back(tmp);
        }
        for(int j=0;j<N;++j){
            char cur;
            cur = words[j][0];
            parse[j].push_back(make_pair((int) cur,0));
            for(int k=0;k<words[j].length();++k){
                cur = words[j][k];
                parse[j][parse[j].size()-1].second++;
                if(k+1<words[j].length()){
                    if(cur!=words[j][k+1]){
                        parse[j].push_back(make_pair((int) words[j][k+1],0));
                    }
                }
            }
        }
        //Dump parse for debugging
        /*for(int q=0;q<N;++q){
            for(int r=0;r<parse[q].size();++r){
                printf("( %c, %d)|",(char) parse[q][r].first,parse[q][r].second);
            }
            printf("\n");
        }*/
        
        for(int a=0;a<N-1;++a){
            if(parse[a].size()!=parse[a+1].size()) win=false;
        }
        if(win){
            for(int b=0;b<parse[0].size();++b){
                for(int c=0;c<N-1;++c){
                    if(parse[c][b].first!=parse[c+1][b].first) win=false;
                }
            }
            if(win){
                int totMoves=0;
                for(int b=0;b<parse[0].size();++b){
                    int tmpTot=0;
                    int tmpAvg=0;
                    int tmpMoves=0;
                    for(int c=0;c<N;++c){
                        tmpTot+=parse[c][b].second;
                    }
                    tmpAvg = (int) tmpTot/N;
                    for(int c=0;c<N;++c){
                        tmpMoves+=fabs(parse[c][b].second-tmpAvg);
                    }
                    totMoves+=tmpMoves;
                }
                fout<<"Case #"<<i<<": "<<totMoves<<endl;
            }
            else{
                fout<<"Case #"<<i<<": Fegla Won"<<endl;
            }
        }
        else{
            fout<<"Case #"<<i<<": Fegla Won"<<endl;
        }
        char cur;
    }
    
    scanf("%d",&T);
    return 0;
}
