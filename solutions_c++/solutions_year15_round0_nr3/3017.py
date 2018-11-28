#include<stdio.h>
#pragma warning(disable:4996)

char input[10005];
int result[10005];
int front[10005];
int end[10005];

int mapping(char c){
	if (c == 'i'){
		return 1;
	}
	else if (c == 'j'){
		return 2;
	}
	else 
		return 3;
}
int oper(int x, int y){
	int flag;
	if (x == 0 || y == 0) return 4;
	if (x * y < 0)
		flag = -1;
	else 
		flag = 1;
	if (x == 4)
		return y;
	else if (y == 4)
		return x;

	if (x == -4)
		return -1*y;
	else if (y == -4)
		return -1 * x;

	if (x < 0) x *= -1;
	if (y < 0) y *= -1;
	if (x == y)
		return -4*flag;
	if (x == 1){
		if (y == 2)
			return 3 * flag;
		if (y == 3)
			return -2 * flag;
	}
	if (x == 2){
		if (y == 1)
			return -3 * flag;
		if (y == 3)
			return 1 * flag;
	}
	if (x == 3){
		if (y == 1)
			return 2 * flag;
		if (y == 2)
			return -1 * flag;
	}
}
int mod(__int64 x, int y){
	if (x <= 0){
		return 4;
	}
	if (x % 4 == 1)
		return y;
	if (x % 4 == 2)
		return -4;
	if (x % 4 == 3)
		return -y;
	if (x % 4 == 0)
		return 4;
}
int for_loop(int i,__int64 temp,int all,int l){
	int chk = 0, temp2,j;
	for (j = l - 1; j >= 0; j--){
		if (end[j] == 3 && temp == 0 && j - i > 1){
			if (end[i + 1] == 1){
				chk = 1;
				break;
			}
		}
		if (end[j] == 3 && temp >=1){
			temp2 = mod(temp-1, all);
			if ((i == 0 && oper(oper(end[i + 1], temp2), 4) == 2) || oper(oper(end[i + 1], temp2), front[j - 1]) == 2){
				chk = 1;
				break;
			}
		}
		if (end[j] == -3 && temp >= 2){
			if (temp != 2 || j - i > 1){
				temp2 = mod(temp - 3, all);
				if ((i == 0 && oper(oper(end[i + 1], temp2), 4) == 2) || oper(oper(end[i + 1], temp2), front[j - 1]) == 2){
					chk = 1;
					break;
				}
			}
		}
		if (oper(end[j], all) == 3 && temp >= 1){
			if (temp != 1 || j - i > 1){

				temp2 = mod(temp - 2, all);
				if ((i == 0 && oper(oper(end[i + 1], temp2), 4) == 2) || oper(oper(end[i + 1], temp2), front[j - 1]) == 2){
					chk = 1;
					break;
				}
			}
		}
		if (oper(end[j], all) == -3 && temp >= 3){
			if (temp != 3 || j - i <= 1){
				temp2 = mod(temp - 4, all);
				if ((i == 0 && oper(oper(end[i + 1], temp2), 4) == 2) || oper(oper(end[i + 1], temp2), front[j - 1]) == 2){
					chk = 1;
					break;
				}
			}
		}
	}

	return chk;
}
int main()
{
	FILE *fi = fopen("input.txt", "r");
	FILE *fo = fopen("output.txt", "w");
	int l,i,j,t,p,all,k,chk;
	__int64 x, temp, temp2;

	fscanf(fi,"%d", &t);
	for (p = 1; p <= t; p++){
		fscanf(fi, "%d %I64d", &l, &x);
		fscanf(fi, "%s", input);
		for (i = l; i < l*x; i++){
			input[i] = input[i%l];
		}
		l = l*x, x = 1;
		for (i = 0; i < l; i++)
			result[i] = mapping(input[i]);
		result[l] = 0;
		front[0] = result[0];
		end[l - 1] = result[l - 1];
		for (i = 1; i < l; i++){
			front[i] = oper(front[i - 1], result[i]);
			end[l-1-i] = oper(result[l-1-i], end[l-i]);
		}
		front[l] = end[l] = 0;

		all = front[l - 1];
		chk = 0;
		for (i = 0; i < l; i++){
			temp = x;
				if (front[i] == 1){
					chk = for_loop(i, temp - 1, all,l);
					if (chk == 1)
						break;
				}
				if (front[i] == -1 && temp >= 3){
					chk = for_loop(i, temp - 3, all,l);
					if (chk == 1)
						break;
				}
				if (oper(all, front[i]) == 1 && temp >= 2){
					chk = for_loop(i, temp - 2, all,l);
					if (chk == 1)
						break;
				}
				if (oper(all, front[i]) == -1 && temp >= 4){
					chk = for_loop(i, temp - 4, all,l);
					if (chk == 1)
						break;
				}
		}

		if (chk == 0){
			fprintf(fo,"Case #%d: NO\n", p);
		}
		else {
			fprintf(fo, "Case #%d: YES\n", p);
		}
	}
	return 0;
}