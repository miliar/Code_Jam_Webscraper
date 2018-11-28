#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main(){
    int cases;
    scanf ("%d",&cases);
    vector<int> av;
    vector<int> bv;
    for(int i=1;i<cases+1;i++){
        av.clear();
        bv.clear();
        int a;
        scanf("%d",&a);
        for(int k=0;k<4;k++){
            for(int j=0;j<4;j++){
                int temp;
                scanf("%d",&temp);
                if(k == a-1)
                    av.push_back(temp);
            }
        }
        int b;
        scanf("%d",&b);
        for(int k=0;k<4;k++){
            for(int j=0;j<4;j++){
                int temp;
                scanf("%d",&temp);
                if(k == b-1)
                    bv.push_back(temp);
            }
        }
        vector<int> result(4);
        sort(av.begin(), av.end());
        sort(bv.begin(), bv.end());
        vector<int>::iterator it = set_intersection(av.begin(),av.end(),bv.begin(), bv.end(), result.begin());
        result.resize(it-result.begin());
        if (result.size()==1) {
            printf("Case #%d: %d",i,result[0]);
            printf("\n");
        }
        else if(result.size() == 0){
            printf("Case #%d: Volunteer cheated!",i);
            printf("\n");
        }
        else{
            printf("Case #%d: Bad magician!",i);
            printf("\n");
        }
    }
}
