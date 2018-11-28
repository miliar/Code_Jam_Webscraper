#include<cstdio>

int table[50][50];

int bomb;
int height,width;

int FillCol(int w,int h){
	int i;
	if(bomb >= h){
		for(i=0;i<h;i++) table[i][w-1] = -1;
		return h;
	}else if(bomb == h-1){
		table[h-1][w-2] = -1;
		for(i=0;i<bomb-1;i++) table[h-1-i][w-1] = -1;
		return bomb;
	}else{
		for(i=0;i<bomb;i++) table[h-1-i][w-1] = -1;
		return bomb;
	}
}

int FillRow(int w,int h){
	int i;
	if(bomb >= w){
		for(i=0;i<w;i++) table[h-1][i] = -1;
		return w;
	}else if(bomb == w-1){
		table[h-2][w-1] = -1;
		for(i=0;i<bomb-1;i++) table[h-1][w-1-i] = -1;
		return bomb;
	}else{
		for(i=0;i<bomb;i++) table[h-1][w-1-i] = -1;
		return bomb;
	}
}

void NumTable(){
	int i,j;
	int count;

	for(i=0;i<height;i++){
		for(j=0;j<width;j++){
            if(table[i][j] == 0){
				count = 0;
				if(i > 0){
					if(j > 0 && table[i-1][j-1] == -1) count++;
					if(table[i-1][j] == -1) count++;
					if(j < width-1 && table[i-1][j+1] == -1) count++;
				}

				if(j > 0 && table[i][j-1] == -1) count++;
				if(j < width-1 && table[i][j+1] == -1) count++;

				if(i < height-1){
					if(j > 0 && table[i+1][j-1] == -1) count++;
					if(table[i+1][j] == -1) count++;
					if(j < width-1 && table[i+1][j+1] == -1) count++;
				}
				table[i][j] = count;
            }
		}
	}
}

void ShowTable(){
	int i,j;
	for(i=0;i<height;i++){
		for(j=0;j<width;j++){
			if(i == 0 && j == 0) printf("c");
			else printf("%c",(table[i][j]==-1)?'*':'.');
		}
		printf("\n");
	}

	/*for(i=0;i<height;i++){
		for(j=0;j<width;j++){
			printf("%3d",table[i][j]);
		}
		printf("\n");
	}*/
}

int chkCount;
void Check(int x,int y){
	if(x<0 || y<0 || x>=width || y>=height) return;
	if(table[y][x] == -1 || table[y][x] == 10) return;
	int chk = (table[y][x] == 0);
	table[y][x] = 10;
	if(chk){
		Check(x+1,y+1);
		Check(x+1,y);
		Check(x+1,y-1);

		Check(x,y+1);
		Check(x,y-1);

		Check(x-1,y+1);
		Check(x-1,y);
		Check(x-1,y-1);
	}
    chkCount++;
}

int main(){
	int testcase,tc;

	int curWidth,curHeight;
	int i,j;
	int oldBomb;

	scanf("%d",&testcase);
	for(tc=1;tc<=testcase;tc++){
		scanf("%d %d %d",&height,&width,&bomb);
		oldBomb = bomb;

		//Init
		curHeight = height;
		curWidth = width;
		for(i=0;i<height;i++) for(j=0;j<width;j++) table[i][j] = 0;

		while(bomb > 0){
			if(curWidth > curHeight){
				bomb -= FillCol(curWidth,curHeight);
				curWidth--;
			}else{
				bomb -= FillRow(curWidth,curHeight);
				curHeight--;
			}
		}

		NumTable();
		chkCount = 0;
		Check(0,0);

		printf("Case #%d:\n",tc);
		if(chkCount+oldBomb != width*height) printf("Impossible\n");
		else ShowTable();
	}

	return 0;
}
