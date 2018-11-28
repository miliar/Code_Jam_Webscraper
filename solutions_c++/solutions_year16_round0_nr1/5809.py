#include <iostream>
#include <cstdio>

using namespace std;

int main(){

freopen("A-large.in","r",stdin);
freopen("resultQ1.txt","w",stdout);

int num;

cin >> num;

for (int times = 1; times <= num; times++){
    int N;
    cin >> N;
    if(N == 0){
        cout << "Case #" << times << ": INSOMNIA" << endl;
    }else{
        bool done = false;
        int store[10];
        for(int i = 0; i < 10; i++){
            store[i] = 0;
        }
        int counter = 1;
        int change = N;
        while(!done){
            counter++;
            int temp = change;
            while(temp != 0){
                store[temp%10]++;
                temp = temp/10;
            }
            bool check = false;
            for(int i = 0 ; i < 10 && check == false; i++){
                if(store[i] == 0){
                    check = true;
                }
            }
            if(check == false){
                cout << "Case #" << times << ": " << change << endl;
                done = true;
            }else{
                change = N*counter;
            }
        }
    }
}

return 0;
}
