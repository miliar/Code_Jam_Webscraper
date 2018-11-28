#include <bits/stdc++.h>

using namespace std;

struct party{
    char what;
    int howmany;
};

bool cmp(party a, party b){
    return a.howmany>b.howmany;
}

int main(){
    freopen("A-large.in","r",stdin); freopen("00_output.txt","w",stdout);

    int t;
    scanf("%d",&t);
    for(int tc=1;tc<=t;tc++){
        int n;
        scanf("%d",&n);
        party letters[26];
        for(int i=0;i<n;i++){
            letters[i].howmany=0;
        }
        int total=0;
        for(int i=0;i<n;i++){
            letters[i].what='A'+i;
            scanf("%d",&letters[i].howmany);
            total+=letters[i].howmany;
        }
        printf("Case #%d: ",tc);
        while(total>0){
            sort(letters,letters+n,cmp);
            int tmp1=total-1;
            bool ok=false;
            if (letters[1].howmany>0 && letters[1].howmany==letters[0].howmany){
                //    cout<<"reaching if"<<endl;
                tmp1--;
                ok=true;
                for(int i=2;i<n;i++){

                    if (letters[i].howmany>tmp1/2){
                        ok=false;
                    }
                }
            }
            if (ok){
               // cout<<"its ok\n";
                letters[0].howmany--;
                letters[1].howmany--;
                total-=2;
                printf("%c%c ",letters[0].what,letters[1].what);
            }
            else {
                letters[0].howmany--;
                total--;
                printf("%c ",letters[0].what);
            }

        }
        printf("\n");

    }

}
