#include<stdio.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<map>
#include <iostream>     // std::cout
#include <fstream>   
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(!head) return head;
        
        ListNode *a, *b;
        a = head;
        b = head->next;
        while((a) && (b)){
            printf("Start with a:%d, b:%d \n", a->val, b->val);
            a->next = b->next;
            printf("temp a:%d bnext:d\n", a->val);
            b->next = a;
            printf("New next vals a:%d, b:%d \n", a->next->val, b->next->val);
            a = a->next;
            b = a->next;
        }
        return head->next;
    }
};


class xyz{
public:
    int abcd;
    xyz(int value)
    {
       abcd = value;
    }
};

class node{
private:
public:
    int data;
    int test_val;
    int test_val1;
    int test_val2;
    node* next;
//    void append(node* tail){
//        node* root = this;
//        while(root->next != NULL){
//            root = root->next;
//        }
//        root->next = tail;
//    }

    node(int value)
    {
        data = value;
        next = 0;
    }

    ~node(){}
};

//void removeDups(node *root){
//   map<int, bool> dataMap;
//   node* last = root; 
//   while(root != NULL){
//       if(dataMap.end() == dataMap.find(root->data)){
//           dataMap[root->data] = 1;
//       }else{
//           printf("NN DEBUG: delete:%d \n", root->data);
//           if(root->next != NULL){
//               last->next = root->next;
//           }else{
//               last->next = 0;
//           }
//           delete root;
//           root = last;
//       }
//       last = root;
//       root = root->next;
//   }
//}
//
//void printList(node *root){
//    int i = 0;
//    printf("Node %d: data:%d \n", i, root->data);
//    while(root->next != NULL){
//        root = root->next;
//        i++;
//        printf("Node %d: data:%d \n", i, root->data);
//    }
//}
int digs[10];


void pop(int N){
    while(N != 0){
        //printf("N%d Nmod:%d \n", N, N%10);
        digs[N % 10]++;
        N = N /10; 
    }
}

bool check(){
    for(int i = 0; i < 10; i++){
        if(digs[i] == 0)
            return false;
    }
    return true;
}
void run(int N, int caseNo){
    memset(digs, 0, sizeof(digs));
    int newN = N;
    int i = 1;
    pop(newN);
    if(check()){
        printf("Case #%d: %d \n", caseNo, newN);
        return;
    }
    i++;
    newN = (i)*N;
    while(newN != N){
        //printf("NewN %d \n", newN);
        pop(newN);
        if(check()){
            printf("Case #%d: %d \n", caseNo, newN);
            return;
        }
        i++;
        newN = (i)*N;
    }
    printf("Case #%d: INSOMNIA \n", caseNo);
}

int main(int argc, char**argv){
    int numTest;
    ifstream myfile ("A-large.in.txt");
    myfile >>  numTest;
    for(int i = 0; i < numTest; i++){
        int test_input;
        myfile >> test_input;
        //printf("NN DEBUG: %d\n", test_input);
        run(test_input, i+1);
    }
}
