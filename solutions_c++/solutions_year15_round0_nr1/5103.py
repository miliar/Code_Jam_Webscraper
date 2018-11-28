#pragma warning(disable:4996)
#include <stdio.h>
void printTestcase(int x, int y){
	printf("Case #%d: %d\n", x, y);
}
int main(){
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i){
		int sm;
		scanf("%d", &sm);
		int arr[1000] = { 0 };
		for (int j = 0; j <= sm; ++j){
			scanf("%1d", &arr[j]);
		}
		int standing = 0;
		int friend_ = 0;
		for (int j = 0; j <= sm; ++j){
			while (standing < j){
				++friend_;
				++standing;
			}
			standing += arr[j];
		}
		printTestcase(i + 1, friend_);
	}
	return 0;
}