#include <iostream>

using namespace std;

int tabla1[4][4];
int tabla2[4][4];
int utilizado[17];
int row1,row2;

void resuelve(int caso)
{
    int i,j,k;
    for(i=1;i<=16;i++)
    {
        utilizado[i]=0;
    }
    utilizado[tabla1[row1][0]]++;
    utilizado[tabla1[row1][1]]++;
    utilizado[tabla1[row1][2]]++;
    utilizado[tabla1[row1][3]]++;
    
    
    utilizado[tabla2[row2][0]]++;
    utilizado[tabla2[row2][1]]++;
    utilizado[tabla2[row2][2]]++;
    utilizado[tabla2[row2][3]]++;
    
    int cheat=0;
    int res=0;
    for(i=1;i<=16;i++)
    {
        //cout<< "utilizado " << utilizado[i]<< " " << i <<endl;
        if(utilizado[i]==2)
        {
            cheat++;
            res=i;
        }
    }
    
    if(cheat==0)
    {
        cout << "Case #"<<caso <<": Volunteer cheated!"<<endl;
    }
    else if(cheat==1)
    {
        cout << "Case #"<<caso<<": "<<res<<endl;
    }
    else
    {
        cout << "Case #"<<caso<<": Bad magician!"<<endl;
    }
    
}


int main()
{
    int T;
    cin >> T;
    
    int i,j,k;
    
    for(i=0;i<T;i++)
    {
        cin >> row1;
        row1--; // PAra ajustar al vector que empieza en 0
        for(j=0;j<4;j++)
        {
            cin >> tabla1[j][0] >> tabla1[j][1] >> tabla1[j][2] >> tabla1[j][3];
        }
        cin >> row2;
        
        row2--; // PAra ajustar al vector que empieza en 0
        for(j=0;j<4;j++)
        {
            cin >> tabla2[j][0] >> tabla2[j][1] >> tabla2[j][2] >> tabla2[j][3];
        }
        resuelve(i+1);
        
    }
    return 0;
}
