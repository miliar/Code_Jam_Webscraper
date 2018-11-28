#include <iostream>
#include <map>
#include <math.h>

using namespace std;

int sumrec(int[]);

int main(){
    int  p;

    freopen("A-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> p;
    for(int i=1;i<=p;i++){
        int process[30]={0}, all[30]={0};
        char input[2005];
        cin >> input;
        string inps(input);
        int length = inps.length();

        for(int j=0;j<length;j++){
            process[input[j]-'@']++;
        }


        process['E'-'@']-=process[26];
        process['R'-'@']-=process[26];
        process['O'-'@']-=process[26];
        all[0]+=process[26];
        process['Z'-'@']=0;

        process['T'-'@']-=process['W'-'@'];
        process['O'-'@']-=process['W'-'@'];
        all[2]+=process['W'-'@'];
        process['W'-'@'] = 0;

        process['F'-'@']-=process['U'-'@'];
        process['O'-'@']-=process['U'-'@'];
        process['R'-'@']-=process['U'-'@'];
        all[4]+=process['U'-'@'];
        process['U'-'@'] = 0;

        process['S'-'@']-=process['X'-'@'];
        process['I'-'@']-=process['X'-'@'];
        all[6]+=process['X'-'@'];
        process['X'-'@'] = 0;


        process['E'-'@']-=process['G'-'@'];
        process['I'-'@']-=process['G'-'@'];
        process['H'-'@']-=process['G'-'@'];
        process['T'-'@']-=process['G'-'@'];
        all[8]+=process['G'-'@'];
        process['G'-'@']=0;



        process['T'-'@']-=process['H'-'@'];
        process['R'-'@']-=process['H'-'@'];
        process['E'-'@']-=process['H'-'@'];
        process['E'-'@']-=process['H'-'@'];
        all[3]+=process['H'-'@'];
        process['H'-'@'] = 0;


        process['I'-'@']-=process['F'-'@'];
        process['V'-'@']-=process['F'-'@'];
        process['E'-'@']-=process['F'-'@'];
        all[5]+=process['F'-'@'];
        process['F'-'@']=0;



        process['E'-'@']-=process['S'-'@'];
        process['V'-'@']-=process['S'-'@'];
        process['E'-'@']-=process['S'-'@'];
        process['N'-'@']-=process['S'-'@'];
        all[7]+=process['S'-'@'];
        process['S'-'@'] = 0;

        process['N'-'@']-=process['I'-'@'];
        process['N'-'@']-=process['I'-'@'];
        process['E'-'@']-=process['I'-'@'];
        all[9]+=process['I'-'@'];
        process['I'-'@'] = 0;


        process['O'-'@']-=process['N'-'@'];
        process['E'-'@']-=process['N'-'@'];
        all[1]+=process['N'-'@'];
        process['N'-'@']=0;

        cout << "Case #" << i << ": ";
        for(int j=0;j<10;j++){
            for(int k=0;k<all[j];k++)
                cout << j;
        }
        cout << endl;

    }
    return 0;
}

int sumrec(int process[]){
    int sum = 0;
    for(int i=0;i<30;i++){
        sum += process[i];
    }
    return sum;
}
