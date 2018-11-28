#include<cstdio>
#include<vector>
#include<cstdlib>

using namespace std;

int main(){

    int T, no, Smax, clapping, threshold, invitations;

    scanf("%d", &T);
    no = 0;
    while(T--){
        scanf("%d ", &Smax);
        vector<int> shyness;

        for(int i = 0; i <= Smax; i++){
            shyness.push_back(getchar()%'0');

        }
        //printf("%d  ", shyness.size());
        invitations = clapping = 0;
        for(threshold = 0; threshold <= Smax; threshold++){
            if(threshold <= clapping)
                clapping += shyness[threshold];
            else{
                invitations += threshold - clapping;
                clapping += threshold - clapping;
                clapping += shyness[threshold];
            }
        }
        //shyness.clear();

        no++;
        printf("Case #%d: %d\n", no, invitations);

    }

    return 0;
}
