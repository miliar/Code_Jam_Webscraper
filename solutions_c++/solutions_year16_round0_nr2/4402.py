#include<bits/stdc++.h>
using namespace std;
int main(){
    FILE *myFile;
    myFile = fopen("C:\\Users\\Dell\\Desktop\\input2.in", "r");
    FILE *fptr;
    fptr = fopen("C:\\Users\\Dell\\Desktop\\output.txt","w");
    int t;
    fscanf(myFile, "%d", &t);
    int cc = 1;
    //cin>>t;
    while(t--){
        char s[105];
        fscanf(myFile, "%s", s);
        //cin>>s;
        int n = strlen(s);
        int i;
        long long int ans = 0;
        char curr_symb = s[0];
        for(i = 1; i < n; i++){
            if(s[i] != s[i-1]){
                ans++;
                if(s[i-1] == '+'){
                    curr_symb = '-';
                }
                else{
                    curr_symb = '+';
                }
            }
        }
        if(curr_symb == '-'){
            ans++;
        }
        fprintf(fptr,"Case #%d: %lld\n",cc++,ans);
        //cout<<ans<<"\n";
    }
    fclose(myFile);
    fclose(fptr);
    return 0;
}
