#include<iostream>
#include<algorithm>
#include<cmath>

using namespace std;

int solve(){

    int n;
    cin>>n;

    char *comparedchar;
    int **allcharcount=new int*[n];
    int comparedcount;

    //string alls[n];

    int maxlen=0;

    for(int i=0;i<n;i++){
        string cur;
        cin>>cur;
        //alls[i]=cur;
        
        //first one will need to find all char sequence
        char cchar=cur[0];
        char *allc=new char[cur.length()];
        int *alli=new int[cur.length()];
        int allcount=0;

        int count=1;
        for(int ci=1;ci<cur.length();ci++){
            char c=cur[ci];
            if(c!=cchar){
                allc[allcount]=cchar;       
                alli[allcount]=count;       
                allcount++;
                count=1;
                cchar=c;
            }else{
                count++;
            }
        }
        allc[allcount]=cchar;       
        alli[allcount]=count;       
        allcharcount[i]=alli;
        allcount++;

        if(i==0){
            comparedchar=allc;
            comparedcount=allcount;
        }else{
            if(allcount!=comparedcount || !equal(comparedchar,comparedchar+comparedcount,allc)){
                /*
                cout<<"At "<<i<<endl;
                for(int si=0;si<n;si++){
                    cout<<alls[si]<<endl;
                }
                */
                return -1;
                continue;
            }
        }

    }

    //Now that we know its okay, we can check what is the most practical way to do this.
    //so we check for each column, the average, which is the target
    //then we iterate for each row the amount of step needed to get to it
    int total=0;
    for(int i=0;i<comparedcount;i++){
        int sum=0;
        for(int i2=0;i2<n;i2++){
            sum+=allcharcount[i2][i];
        }
        int togo=round(((double)sum)/n);
        int step=0;
        for(int i2=0;i2<n;i2++){
            step+=abs(allcharcount[i2][i]-togo);
        }
        total+=step;
    }

    return total;

}

int main(int argv,char** argc){

    int testc;
    cin>>testc;

    for(int testi=0;testi<testc;testi++){
        cout<<"Case #"<<testi+1<<": ";
        int ans=solve();
        if(ans==-1){
            cout<<"Fegla Won"<<endl;
        }else{
            cout<<ans<<endl;
        }
    }

    return 0;
}
