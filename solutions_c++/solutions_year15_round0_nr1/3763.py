#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

template <class T> class Queue;
template <class T> ostream& operator<< (ostream&, const Queue<T> &);

template <class T>
class QueueItem {
    friend class Queue<T>;
    friend ostream& operator<< (ostream&, const Queue<T> &);
    QueueItem(const T &t): item(t), next(0) {}
    T item;
    QueueItem *next;
};

template <class T>
class Queue{
public:
    template <class It> Queue(It beg, It end): head(0), tail(0){
        copy_element(beg, end);
    }
    Queue(): head(0), tail(0) {}
    Queue(const Queue &Q): head(0), tail(0){
        copy_element(Q);
    }
    Queue& operator= (const Queue&);
    ~Queue() {destroy();} //?
    template <class Iter> void assign(Iter, Iter);
    T& front() const { return head->item; }
//    const T &front() const { return head->item; }
    void push(const T&);
    void pop ();
    bool empty () const {
        return head == 0;
    }

private:
    QueueItem<T> *head;
    QueueItem<T> *tail;
    void destroy();
    void copy_element(const Queue&);
    template <class Iter> void copy_element(Iter, Iter);
};

template <class T> void Queue<T>::destroy(){
    while(!empty())
        pop();
}

template <class T> void Queue<T>::pop() {
    QueueItem<T> *p = head;
    head = head->next;
    delete p;
}

template <class T> void Queue<T>::push(const T &val) {
    QueueItem<T> *pt = new QueueItem<T>(val);
    if(empty()){
        head = tail = pt;
    }else{
        tail->next = pt;
        tail = pt;
    }
}

template <class T> template <class Iter> void Queue<T>::assign(Iter beg, Iter end) { //template member function
    destroy();
    copy_element(beg, end);
}

template <class T> template <class It> void Queue<T>::copy_element(It beg, It end) { //template member function
    while(beg != end){
        push(*beg);
        ++ beg;
    }
}

template <class T>
ostream& operator<< (ostream &os, const Queue<T> &q){
    os<<"<";
    QueueItem<T> *p;
    for(p = q.head; p; p = p->next){
        os<<p->item<<" ";
    }
    os<<">";
    return os;
}


