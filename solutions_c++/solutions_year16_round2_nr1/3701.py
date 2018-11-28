#include <bits/stdc++.h>
using namespace std;


int main(){
     freopen("output.txt", "w", stdout);
  freopen("input.txt", "r", stdin);
    int t;
    cin>>t;
    for(int qq=1;qq<=t;qq++){

        string s;
        cin>>s;
        
        cout<<"Case #"<<qq<<": ";
        
        int a[10];
        for(int i=0; i<10; i++){
            a[i] = 0;
        } 
        
        int val[26];
        for(int  i=0; i<26; i++){
            val[i] = 0;
        }
        for(int i=0; i<s.length(); i++){
            val[s[i]-'A']++;
        }
        string letters[10]= {
        "ZERO",
        "TWO",
        "SIX",
        "EIGHT",
        "FOUR",
            
        "THREE",
        "SEVEN",
        "FIVE",
        "ONE",
        "NINE"
        };
        int map[10] = {0,2,6,8,4,3,7,5,1,9};
        int temp[26];
        
        int u = s.length()/3;
        for(int t=0; t<u; t++){
            for(int i=0;i<5;i++){
                for(int k=0; k<26; k++){
                    temp[k] = val[k];
                }
                int j;
                for(j=0; j<letters[i].length(); j++){
                    if(temp[letters[i][j] - 'A']){
                        temp[letters[i][j] - 'A']--;
                    }else{
                        break;
                    }
                }
                if(j==letters[i].length()){
                     for(int m=0; m<letters[i].length();m++){
                        val[letters[i][m]-'A']--;
                    }
                    a[i]++;
                }
            }
        }
        for(int t=0; t<u; t++){
            for(int i=5;i<10;i++){
                for(int k=0; k<26; k++){
                    temp[k] = val[k];
                }
                int j;
                for(j=0; j<letters[i].length(); j++){
                    if(temp[letters[i][j] - 'A']){
                        temp[letters[i][j] - 'A']--;
                    }else{
                        break;
                    }
                }
                if(j==letters[i].length()){
                     for(int m=0; m<letters[i].length();m++){
                        val[letters[i][m]-'A']--;
                    }
                    a[i]++;
                }
            }
        }
        int arr[1000];
        int  j=0;
        for(int i=0; i<10; i++){
            while(a[i]){
                arr[j++] = map[i];
                a[i]--;
            }
        }
        sort(arr, arr+j);
        for(int k=0; k<j; k++){
            cout<<arr[k];
        }
        cout<<endl;
    }
    return 0;
}


