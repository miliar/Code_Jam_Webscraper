#include <stdio.h>
#include <stdio.h>

int main()
{
    int T;
    scanf("%d",&T);

    for(int t=1;t<=T;t++){
        int N,M;
        scanf("%d%d",&N,&M);

        int a[N][M];

        int rows[N];
        int cols[M];

        for(int i=0;i<N;i++){
            rows[i]=0;
            for(int j=0;j<M;j++){
                cols[j]=0;
                scanf("%d",&a[i][j]);
            }
        }

        int status = 0;

        while(status == 0){

            bool isYes = true;
            bool isNo = true;

            for(int i=0;i<N;i++){
                if(rows[i] == 0){
                    isYes = false;
                    int trow = -1;
                    int frow = -1;
                    bool isCut = true;

                    for(int j=0;j<M;j++){
                        if(cols[j]==0 ){
                                if(trow == -1) {
                                    trow = a[i][j];
                                }else if(trow != a[i][j]){
                                    isCut = false;
                                    break;
                                }
                        }else{
                            if(a[i][j] > frow)
                                frow = a[i][j];
                        }
                    }
                    if(isCut && trow > -1 && frow > trow){
                        isCut = false;
                    }

                    if(isCut){
                        rows[i]=1;
                        isNo = false;
                    }
                }
            }

            for(int j=0;j<M;j++){
                if(cols[j] == 0){
                    isYes = false;
                    int tcol = -1;
                    int fcol = -1;
                    bool isCut = true;

                    for(int i=0;i<N;i++){
                        if(rows[i]==0 ){
                                if(tcol == -1) {
                                    tcol = a[i][j];
                                }else if(tcol != a[i][j]){
                                    isCut = false;
                                    break;
                                }
                        }else{
                            if(a[i][j] > fcol)
                                fcol = a[i][j];
                        }
                    }
                    if(isCut && tcol > -1 && fcol > tcol){
                        isCut = false;
                    }

                    if(isCut){
                        cols[j]=1;
                        isNo = false;
                    }
                }
            }

            if(isYes){
                status = 1;
            }else if(isNo){
                status = 2;
            }
        }

        if(status == 1){
            printf("Case #%d: YES\n",t);
        }else if(status == 2){
            printf("Case #%d: NO\n",t);
        }
    }
}
