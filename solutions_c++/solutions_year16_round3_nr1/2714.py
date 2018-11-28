#include<bits/stdc++.h>
using namespace std;


int ara[27]={0};

void init(){
    for(int k = 0; k < 27; k++){
        ara[k] = 0;
    }
}

int find_max(){
    int maxx = 0, maxx_i = -1;
    for(int k = 0; k < 26; k++){
        if(ara[k] > maxx){
            maxx = ara[k];
            maxx_i = k;
        }
    }
    return maxx_i;
}

int find_s_max(int skip){
    int maxx = 0, maxx_i = -1;
    for(int k = 0; k < 26; k++){
        if(k == skip)continue;
        if(ara[k] > maxx){
            maxx = ara[k];
            maxx_i = k;
        }
    }
    return maxx_i;
}

int main(){

    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T,N;
    cin >> T;

    for(int k = 0; k < T; k++){

        init();

        cin >> N;
        int sum = 0;
        for(int l = 0; l < N; l++){
            cin >> ara[l];
            sum+=ara[l];
        }

        cout << "Case #" << k+1 << ": ";

        int cc = 0;
        if( sum % 2 ){
            int mm = find_max();
            ara[mm]--;
            printf("%c",mm+'A');
            cc++;
            if(sum!=cc)cout << " ";
        }

        while(1){
            int max1 = find_max();
            if(max1 == -1)break;
            int max2 = find_s_max(max1);
            ara[max1]--;
            //cout << max1;
            printf("%c",max1+'A');
            cc++;
            if(max2!=-1){
                ara[max2]--;
                printf("%c",max2+'A');
                cc++;
            }
            if(sum!=cc)cout << " ";
        }
        cout << endl;

    }






 //   cout << max1 << " " << max2 << endl;

}
