#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

//using namespace std;

int main(int argc, char** argv)
{
	int T, R, C,W;
	scanf("%d\n",&T);
	int result;
	int c,r, rem;
	for(int t=0;t<T;t++)
	{	
		scanf("%d %d %d\n",&R,&C,&W);
		c = (C-W)/W;
	
		if((C-W)%W != 0)
		{
			c++;
		}
		r = R;
		result = c*r+W;
		if(W==1) result=R*C;
		//if(W>C)
		//{
		//	result += W;
		//} else {
		//	result += W-1;
		//}
		printf("Case #%d: %d\n",t+1,result);
	}


	return 0;
}
