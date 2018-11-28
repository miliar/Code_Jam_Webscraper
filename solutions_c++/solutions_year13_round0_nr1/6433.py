#include <cstdio>
#include <cstring>

using namespace std;

char a[5][5];
long t,ct,i,j;

bool checkX (void)
{
	bool ok=true;
	long i,j;
	
	for(i=1;i<=4;i++)
		if(a[i][4]!='X')
			if(a[i][4]!='T')
			{
				ok=false;
				break;
			}
	if(ok==true)
		return true;
	ok=true;
	
	for(i=1;i<=4;i++)
		if(a[4][i]!='X')
			if(a[4][i]!='T')
			{
				ok=false;
				break;
			}
	if(ok==true)
		return true;
	ok=true;
	
	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
			if(i+j==5)
				if(a[i][j]!='X')
					if(a[i][j]!='T')
					{
						ok=false;
						break;
					}
	if(ok==true)
		return true;
	ok=true;
	
	for(i=1;i<=4;i++)
		if(a[i][i]!='X')
			if(a[i][i]!='T')
			{
				ok=false;
				break;
			}
			
	if(ok==true)
		return true;
	ok=true;
	for(j=1;j<=4;j++)
	{
		ok=true;
	for(i=1;i<=4;i++)
		if(a[j][i]!='X')
			if(a[j][i]!='T')
			{
				ok=false;
				break;
			}
			if(ok==true)
				break;
	}
	if(ok==true)
		return true;
	ok=true;
	for(i=1;i<=4;i++){
		ok=true;
		for(j=1;j<=4;j++)
			if(a[j][i]!='X')
				if(a[j][i]!='T')
				{
					ok=false;
					break;
				}
		if(ok==true)
			break;
	}
	if(ok==true)
		return true;
	return false;

}

bool checkO (void)
{
	bool ok=true;
	
	for(i=1;i<=4;i++)
		if(a[i][4]!='O')
			if(a[i][4]!='T')
			{
				ok=false;
				break;
			}
	if(ok==true)
		return true;
	ok=true;
	
	for(i=1;i<=4;i++)
		if(a[4][i]!='O')
			if(a[4][i]!='T')
			{
				ok=false;
				break;
			}
	if(ok==true)
		return true;
	ok=true;
	
	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
			if(i+j==5)
				if(a[i][j]!='O')
					if(a[i][j]!='T')
					{
						ok=false;
						break;
					}
	if(ok==true)
		return true;
	ok=true;
	
	for(i=1;i<=4;i++)
		if(a[i][i]!='O')
			if(a[i][i]!='T')
			{
				ok=false;
				break;
			}
			
	if(ok==true)
		return true;
	ok=true;
	
	for(j=1;j<=4;j++)
	{
		ok=true;
	for(i=1;i<=4;i++)
		if(a[j][i]!='O')
			if(a[j][i]!='T')
			{
				ok=false;
				break;
			}
			if(ok==true)
				break;
	}
	if(ok==true)
		return true;
	ok=true;
	for(i=1;i<=4;i++){
		ok=true;
		for(j=1;j<=4;j++)
			if(a[j][i]!='O')
				if(a[j][i]!='T')
				{
					ok=false;
					break;
				}
		if(ok==true)
			break;
	}
	if(ok==true)
		return true;
	return false;
}

int main () {
	
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	scanf("%ld\n",&t);
	long ct=0;
	
	while(t--)
	{
		ct++;
		
		bool setPoint=false;
		
		memset(a,0,sizeof(a));
		
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%c",&a[i][j]);
				if(a[i][j]=='.')
					setPoint=true;
			}
			scanf("\n");
		}
		scanf("\n");
		if(checkX()){
			printf("Case #%ld: X won\n",ct);
			continue;
		}
		if(checkO()){
			printf("Case #%ld: O won\n",ct);
			continue;
		}
		if(setPoint){
			printf("Case #%ld: Game has not completed\n",ct);
			continue;
		}
		printf("Case #%ld: Draw\n",ct);
	}
	return 0;
}
