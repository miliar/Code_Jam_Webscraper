#include <iostream>

using namespace std;

int main(void){
int t;
cin>>t;
for(int n=1;n<=t;n++){
    int num,score1=0,score2=0;
    double naomi[1000],ken[1000];
    cin>>num;
 
    for(int i=0;i<num;i++){
        cin>>naomi[i];
    }
    for(int i=0;i<num;i++){
        cin>>ken[i];
    }
    for(int i=0;i<num-1;i++){
        int k=i;
        for(int j=i+1;j<num;j++){
            if(naomi[k] > naomi[j])
                k=j;
        }
        if(i != k){
            double temp=naomi[i];
            naomi[i]=naomi[k];
            naomi[k]=temp;
        }
    }
    for(int i=0;i<num-1;i++){
        int k=i;
        for(int j=i+1;j<num;j++){
            if(ken[k] > ken[j])
                 k=j;
        }
        if(i != k){
            double temp=ken[i];
            ken[i]=ken[k];
            ken[k]=temp;
        }
    }


    //after sorted if cheated
    for(int i=0,j=0;i<num;i++){
        if(naomi[i] > ken[j]){
            //ken use the smallest one
            score1++;
            j++;
        }
    }

    //after sorted if not cheated
    int k=0;
    for(int i=0;i<num;i++){
        double key=naomi[i];
        for(int j=k;j<num;j++){
            if(ken[j] > key){
                score2++;
                k=j+1;
                break;
            }
        }
    }
    score2=num-score2;
    cout<<"Case #"<<n<<": "<<score1<<" "<<score2<<endl;
}
return 0;
}
