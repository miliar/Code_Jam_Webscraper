#include<iostream>
using namespace std;

int a[4][4],b[4][4];

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("pa.txt","w",stdout);
	int c,cases,t,i,j,ans,first_answer,Second_answer;
	scanf("%d",&cases);
	for(c=1 ; c<=cases ; c++){
		
        scanf("%d",&first_answer);
        first_answer--;
		for(i=0 ; i<4 ; i++){
			scanf("%d%d%d%d",&a[i][0],&a[i][1],&a[i][2],&a[i][3]);
		}
        
        scanf("%d",&Second_answer);
        Second_answer--;
		for(i=0 ; i<4 ; i++){
			scanf("%d%d%d%d",&b[i][0],&b[i][1],&b[i][2],&b[i][3]);
		}
        int count=0;
    
		for (i=0; i<4; i++) {
            for(j=0;j<4;j++){
                if(a[first_answer][i]==b[Second_answer][j])
                {
                    count++;
                    ans=a[first_answer][i];
                }
            }
        }
        switch (count) {
            case 0:
                cout << "Case #" << c << ": Volunteer cheated!" << endl;

                break;
                
            case 1:
                cout << "Case #" << c << ": " << ans << endl;
                
                break;
            default:
                cout << "Case #" << c << ": Bad magician!" << endl;

                break;
        }
	}
}
