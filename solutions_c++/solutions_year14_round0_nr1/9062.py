#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("A-small-attempt4.in");
ofstream fout("A-small-attempt4.out");

int main(){
    int numcase;
    fin>>numcase;

    int array1[4][4];
    int array2[4][4];

    int firstchoose;
    int secondchoose;

    int selectrow[4];
    int tmp,x;
    int count;
    int countcase = 1;
    int hit;
    int i,j;

    while(countcase<=numcase){
            count = 0;

            fin>>firstchoose;
            tmp = (firstchoose-1)*4;
            while(tmp--)fin>>x;
            for(i=0;i<4;++i)
            {
                fin>>selectrow[i];
                }

            tmp = (4-firstchoose)*4;
            while(tmp--)fin>>x;

            fin>>secondchoose;
            tmp = (secondchoose-1)*4;
            while(tmp--)fin>>x;
            for(i=0;i<4;++i){
                fin>>x;

                for(j=0;j<4;++j){
                    if(selectrow[j]==x){
                        count++;
                        hit = x;

                        break;
                    }
                }
            }

            tmp = (4-secondchoose)*4;
            while(tmp--)fin>>x;

            if(count==1){
                //cout<<"Case #"<<countcase<<": "<<hit<<endl;
                fout<<"Case #"<<countcase<<": "<<hit<<endl;
            }
            else if(count == 0){
                //cout<<"Case #"<<countcase<<": "<<hit<<endl;
                fout<<"Case #"<<countcase<<": Volunteer cheated!"<<endl;
            }
            else{
                //cout<<"Case #"<<countcase<<": "<<hit<<endl;
                fout<<"Case #"<<countcase<<": Bad magician!"<<endl;
            }
            countcase++;
    }
}
