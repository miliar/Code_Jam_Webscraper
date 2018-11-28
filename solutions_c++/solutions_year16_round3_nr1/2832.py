#include <bits/stdc++.h>
using namespace std;
int senate[30];
typedef pair <int,int> pi;
vector <int> answers;
vector <char> other;
vector <int> good;
vector <string> printout;
int t;
int n;
int main()
{
    freopen("goodin.txt","r",stdin);
    freopen("goodout.txt","w",stdout);
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        answers.clear();
        other.clear();
        good.clear();
        printout.clear();
        scanf("%d",&n);
        int total = 0;
        for(int j=0;j<n;j++){
            scanf("%d",&senate[j]);
            total += senate[j];
        }
        while(true){
            int curmax = -1;
            int point = -1;
            for(int j=0;j<n;j++){
                if(senate[j]>curmax){
                    curmax = senate[j];
                    point = j;
                }
            }
            //cout << curmax << endl;
            if(curmax==0)break;
            senate[point]--;
            total--;
            answers.push_back(point);
            other.push_back('A'+point);
            curmax = -1;
            point = -1;
            for(int j=0;j<n;j++){
                if(senate[j]>curmax){
                    curmax = senate[j];
                    point = j;
                }
            }
            if(curmax<=total/2){
                good.push_back(1);
            }
            else{
                good.push_back(0);
            }
        }
        vector <string> mystuff;
        int counter = 0;
        bool bad = false;
        while(counter<good.size()){
            //cout << counter << " " << good[counter] << endl;
            if(good[counter]==1){
                string ss = "";
                ss += other[counter];
                printout.push_back(ss);
                counter++;
            }
            else if(counter+1<good.size()&&good[counter+1]==1){
                string ss = "";
                ss += other[counter];
                ss += other[counter+1];
                //cout << ""+other[counter]+other[counter+1] << endl;
                printout.push_back(ss);
                counter += 2;
            }
            else{
                bad = true;
                break;
            }
        }
        if(!bad){
            cout << "Case #" << i+1 << ":" << " ";
            for(int k=0;k<printout.size();k++){
                cout << printout[k] << " ";
            }
        }
        cout << endl;
    }
    //cout << "Hello world!" << endl;
    return 0;
}
