#include <cstdio>
#include <string>

//INPUT
int T, SMAX;
char audience[1005];




void process(const int& t){
	int clapping_count = 0;
	int total_friends = 0;
	int invited_friends = 0;

	int addition = 0;


	for(int i = 0; i <= SMAX; i++)
	{
		addition = int(audience[i]-'0');
		if(i > clapping_count && addition>0) // => We need to invite friends
		{
			invited_friends = (i - clapping_count);
			total_friends += invited_friends;
			clapping_count += invited_friends;

		}

		clapping_count += addition;
	}

	printf("Case #%d: %d\n",t+1,total_friends);



}


int main(int argc, char** argv){


	scanf("%d", &T);

	for(int t = 0; t < T; t++)
	{
		scanf("%d %s",&SMAX,audience);

		process(t);
	}



	return 0;
}